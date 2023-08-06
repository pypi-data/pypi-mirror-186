import importlib
import logging
import os
from unittest.mock import patch
import sys

from openapi_schema_pydantic import OpenAPI
import re

import yaml
import typing as tp

from pydantic import BaseModel, PydanticSchema
from pydantic.schema import schema, model_schema, field_schema, model_process_schema
from satella.coding import silence_excs
from satella.coding.sequences import choose


logger = logging.getLogger(__name__)


def make_doodad() -> tp.Callable:
    def doodad(event: tp.Dict[str, tp.Any]) -> tp.Dict[str, tp.Any]:
        pass

    setattr(doodad, '__name__', 'doodad')
    return doodad


class ServerlessFunction:
    def __init__(self, yaml_desc: dict, prefix_path: tp.Optional[str]):
        self.old_path = sys.path
        self.handler = yaml_desc['Properties']['Handler']
        self.handler_fixes = self.handler.replace('.lambda_handler.handler', '.models')
        self.code_uri = yaml_desc['Properties']['CodeUri']
        self.prefix_path = prefix_path
        self.descr = yaml_desc['Properties'].get('Description')
        self.url = choose(lambda y: y['Type'] == 'Api', yaml_desc['Properties']['Events'].values())['Properties']['Path']
        self.keyword_arguments = [y for y in re.findall('\{.*\}', self.url) if y.strip()]
        self.method = choose(lambda y: y['Type'] == 'Api', yaml_desc['Properties']['Events'].values())['Properties']['Method']

    @silence_excs(ModuleNotFoundError, AttributeError, returns='<unavailable>')
    def get_description(self) -> str:
        """Either load the description from Properties.Description or read in pydoc"""
        return self.descr

    @staticmethod
    def get_annotations_for(cls) -> tp.Set[BaseModel]:
        values = set()
        for value in cls.__annotations__.values():
            if not issubclass(value,  BaseModel):
                continue
            values.add(value)
        return values

    @silence_excs(ModuleNotFoundError)
    def get_get_handler(self):
        sys.path = self.old_path
        sys.path.append(os.path.join(self.prefix_path, self.code_uri))
        try:
            mod = importlib.import_module(self.handler_fixes)
        except ModuleNotFoundError:
            mod = importlib.import_module(self.handler_fixes.replace('.models', '.lambda_handler.handler'))
        sys.reload(mod)
        for cls_name in dir(mod):
            if issubclass(getattr(mod, cls_name), BaseModel):
                annot = annot.intersection(self.get_annotations_for(getattr(mod, cls_name)))
        annot = list(annot)[0]

        v = annot.schema_json_of(indent=2)
        print('returning ', v)
        return v

    @silence_excs(ModuleNotFoundError, AttributeError)
    def get_models_handler(self):
        c_uri = self.code_uri
        if self.prefix_path is not None:
            c_uri = os.path.join(self.prefix_path, c_uri)
        sys.path = self.old_path
        sys.path.append(c_uri)
        mod = importlib.import_module(self.handler_fixes)
        sys.reload(mod)
        pv = getattr(mod, 'parse_event').__annotations__['return'].schema(indent=2) # throws ModuleNotFoundError
        print(pv)
        return pv

    def to_yaml(self) -> tp.Dict:
        parameters = [{'in': 'query', 'name': param.replace('{', '').replace('}', '')} for param in self.keyword_arguments]
        for param in parameters:
            if param['in'] == 'path':
                param['in'] = 'query'
                param['required'] = 'false'
        p = {self.url: {self.method: {'summary': self.get_description()}}}
        params = [param for param in parameters if param]
        if params:
            p[self.url][self.method]['parameters'] = params
        return_s = self.get_get_handler()
        mod_s = self.get_models_handler()
        if mod_s is not None:
            p[self.url][self.method]['requestBody'] = mod_s
        if return_s is not None:
            p[self.url][self.method]['responses'] = {'200': {'content': {'application/json': return_s}}}
        return p


class ServiceLayer:
    def __init__(self, yaml_desc, prefix_path: tp.Optional[str] = None):
        self.content_uri = yaml_desc['Properties']['ContentUri']
        self.prefix_path = prefix_path

    def add_to_path(self) -> None:
        """Add ServiceLayer to PYTHONPATH to enable modules to import"""
        c_uri = self.content_uri
        if self.prefix_path is not None:
            c_uri = os.path.join(self.prefix_path, c_uri)
        sys.path.append(c_uri)

    def __repr__(self):
        return f'ServiceLayer({self.content_uri}'


class SetOfHandlers(tp.Iterator[tp.Union[ServerlessFunction, ServiceLayer]]):
    def __iter__(self):
        return iter(self.handlers)

    def __next__(self):
        return next(self.handlers)

    def __init__(self, handlers: tp.Iterator[tp.Union[ServerlessFunction, ServiceLayer]]):
        self.handlers = list(handlers)
        self.get_service_layer().add_to_path()

    def get_service_layer(self) -> ServiceLayer:
        return choose(lambda y: isinstance(y, ServiceLayer), self.handlers)

    def get_serverless_functions(self) -> tp.Iterator[ServerlessFunction]:
        for serverless_function in self.handlers:
            if isinstance(serverless_function, ServerlessFunction):
                print(repr(serverless_function))
                yield serverless_function


def read_template(func_path: str, tpl_dir: str) -> SetOfHandlers:
    tpl_path = os.path.join(tpl_dir, 'template.yaml')
    with open(tpl_path, 'r') as f_in:
        data = yaml.load(f_in, Loader=yaml.BaseLoader)

    handlers = []
    for datum, values in data['Resources'].items():
        if values['Type'] == 'AWS::Serverless::Function':
            handlers.append(ServerlessFunction(values, os.path.join(tpl_dir, func_path)))
        elif values['Type'] == 'AWS::Serverless::LayerVersion':
            handlers.append(ServiceLayer(values, os.path.join(tpl_dir, func_path)))
    return SetOfHandlers(handlers)
