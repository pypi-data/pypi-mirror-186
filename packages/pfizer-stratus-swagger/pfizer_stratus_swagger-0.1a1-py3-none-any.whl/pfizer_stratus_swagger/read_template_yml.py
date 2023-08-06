import abc
import collections
import io
from immutabledict import immutabledict

import yaml
from ruamel.yaml import YAML
import importlib
import inspect
import logging
import os
import sys

import pydantic
from pydantic import BaseModel, Field, schema_json_of

from openapi_schema_pydantic import OpenAPI
import re

import typing as tp

from openapi_schema_pydantic.util import PydanticSchema
from pydantic import BaseModel
from pydantic.fields import ModelField
from pydantic.schema import schema, model_schema, field_schema, model_process_schema
from pydantic.utils import Representation
from satella.coding import silence_excs, for_argument
from satella.coding.sequences import choose
from satella.coding.structures import frozendict

logger = logging.getLogger(__name__)

def do_yaml(y) -> str:
    yaml = YAML(typ='safe')
    io_text = io.StringIO()
    yaml.dump(y, io_text)
    return io_text.read()


def make_doodad() -> tp.Callable:
    def doodad(event: tp.Dict[str, tp.Any]) -> tp.Dict[str, tp.Any]:
        pass

    setattr(doodad, '__name__', 'doodad')
    return doodad


class ServerlessFunction:
    def __init__(self, yaml_desc: dict, prefix_path: str):
        self.old_path = sys.path
        self.handler = yaml_desc['Properties']['Handler']
        self.handler_fixes = self.handler.replace('.lambda_handler.handler', '.models')
        self.handler_cut = self.handler.replace('.handler', '')
        self.code_uri = os.path.realpath(os.path.join(prefix_path, yaml_desc['Properties']['CodeUri'])).replace('./', '').replace('/', os.path.sep)
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
    def get_annotations_for(cls) -> tp.Iterator[BaseModel]:
        for value in inspect.signature(cls).annotations.values():
            if isinstance(value, BaseModel):
                yield value

    @silence_excs(ModuleNotFoundError)
    def get_get_handler(self):
        """
        Return response schema

        Three options are possible:

        1. parse_event returns a result annotation
        2. All BaseModel needs to be scanned to pick the best one
        """
        sys.path = self.old_path
        sys.path.append(self.code_uri)
        # Try to import parse_event
        mod = importlib.import_module(self.handler_fixes)
        importlib.reload(mod)
        try:
            parse_event = getattr(mod, 'parse_event')
            return parse_event.__annotations__['return'].schema()
        except AttributeError:
            # Get all BaseModels
            class_count = collections.defaultdict(lambda: 0)
            items = [getattr(mod, fname) for fname in dir(mod)]
            for base_model in [y for y in items if type(y) == pydantic.main.ModelMetaclass]:
                if base_model.__class__.__name__ == 'BaseModel':
                    continue
                for annotations, annot_val in base_model.__fields__.items():
                    return base_model.schema()

            elems = list(class_count.items())
            elems.sort(key=lambda y: y[1], reverse=True)
            print(elems)
            out = io.StringIO()
            for annot in class_count:
                out.write(f'{annot}:\n')
                aval = class_count[annot]
                out.write(f'{annot}\n')
            return out.read()

    @silence_excs(ModuleNotFoundError, AttributeError)
    def get_models_handler(self):
        """Return request schema"""
        sys.path = self.old_path
        sys.path.append(self.code_uri)
        mod = importlib.import_module(self.handler_fixes)
        importlib.reload(mod)
        try:
            parse_event = getattr(mod, 'parse_event')
            return inspect.signature(parse_event).annotations['return'].schema() # throws ModuleNotFoundError
        except (AttributeError, KeyError) as e:
            # Get all BaseModels
            class_count = collections.defaultdict(lambda: 0)
            if hasattr(mod, 'models'):
                mod = getattr(mod, 'models')
            items = [getattr(mod, f_name) for f_name in dir(mod)]
            for base_model in [y for y in items if type(y) == pydantic.main.ModelMetaclass]:
                if base_model.__class__.__name__ == 'BaseModel':
                    continue
                return base_model.schema()

    def to_yaml(self) -> tp.Dict:
        parameters = [{'in': 'query', 'name': param.replace('{', '').replace('}', '')} for param in self.keyword_arguments]
        for param in parameters:
            if param['in'] == 'path':
                param['in'] = 'query'
                param['required'] = 'true'
        p = {self.url: {self.method: {'summary': self.get_description()}}}
        params = [param for param in parameters if param]
        if params:
            p[self.url][self.method]['parameters'] = params
        mod_s = self.get_models_handler()
        print(mod_s)
        return_s = self.get_get_handler()
        print(return_s)

        if mod_s is not None:
            p[self.url][self.method]['requestBody'] = {'content': {'application/json': mod_s}}
        if return_s is not None:
            p[self.url][self.method]['responses'] = {'200': {'content': {'application/json': return_s}}}
        return p


class ServiceLayer:
    def __init__(self, yaml_desc, prefix_path: str):
        self.content_uri = yaml_desc['Properties']['ContentUri'].replace('./', '').replace('/', os.path.sep)
        self.prefix_path = prefix_path

    def add_to_path(self) -> None:
        """Add ServiceLayer to PYTHONPATH to enable modules to import"""
        c_uri = os.path.realpath(os.path.join(self.prefix_path, self.content_uri))
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
                yield serverless_function


def read_template(func_path: str, tpl_dir: str) -> SetOfHandlers:
    tpl_path = os.path.join(tpl_dir, 'template.yaml')
    with open(tpl_path, 'r') as f_in:
        data = yaml.load(f_in, Loader=yaml.BaseLoader)

    handlers = []
    for datum, values in data['Resources'].items():
        if values['Type'] == 'AWS::Serverless::Function':
            handlers.append(ServerlessFunction(values, tpl_dir))
        elif values['Type'] == 'AWS::Serverless::LayerVersion':
            handlers.append(ServiceLayer(values, tpl_dir))
    return SetOfHandlers(handlers)
