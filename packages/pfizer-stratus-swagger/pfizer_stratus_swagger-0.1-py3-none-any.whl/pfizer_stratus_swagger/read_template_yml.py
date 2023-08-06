import yaml
import importlib  # because most lambdas are not valid Python packages due to lacking __init__.py
import inspect
import logging
import os
import sys

import pydantic

import re

import typing as tp

from pydantic import BaseModel
from pydantic.schema import model_schema
from satella.coding import silence_excs
from satella.coding.sequences import choose

logger = logging.getLogger(__name__)


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

    def get_models(self) -> tp.Sequence[BaseModel]:
        sys.path = self.old_path
        sys.path.append(self.code_uri)
        # Try to import parse_event
        try:
            mod = importlib.import_module(self.handler_fixes)
        except ImportError:
            return []
        importlib.reload(mod)
        candidates = [getattr(mod, item) for item in dir(mod)]
        models = []
        for candidate in candidates:
            try:
                if issubclass(candidate, BaseModel):
                    models.append(candidate)
            except TypeError:
                # this is because modules contain things that are even not classes and issubclass will TypeError
                continue
        return models

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
        3. None of this applies and we need to make an wild/educated guess
        """
        sys.path = self.old_path
        sys.path.append(self.code_uri)
        # Try to import parse_event
        mod = importlib.import_module(self.handler_fixes)
        importlib.reload(mod)
        try:
            parse_event = getattr(mod, 'parse_event')
            schema = model_schema(parse_event.__annotations__['return'])
            return schema
        except AttributeError as e:
            try:
                schema = choose(lambda y: issubclass(y, BaseModel), [getattr(mod, item) for item in dir(mod)])
                return model_schema(schema)
            except ValueError as e:
                for item in dir(mod):
                    base_model = getattr(mod, item)
                    if hasattr(base_model, '__root__'):
                        schema = model_schema(base_model)
                        return schema

    @silence_excs(ModuleNotFoundError, AttributeError)
    def get_models_handler(self):
        """Return request schema"""
        sys.path = self.old_path
        sys.path.append(self.code_uri)
        mod = importlib.import_module(self.handler_fixes)
        importlib.reload(mod)
        try:
            parse_event = getattr(mod, 'parse_event')
            p = inspect.signature(parse_event).annotations['return'] # throws ModuleNotFoundError
            p = model_schema(p)
            return p
        except (AttributeError, KeyError) as e:
            # Get all BaseModels
            if hasattr(mod, 'models'):
                mod = getattr(mod, 'models')
            items = [getattr(mod, f_name) for f_name in dir(mod)]
            for base_model in [y for y in items if type(y) == pydantic.main.ModelMetaclass]:
                schema = model_schema(base_model)
                if schema['title'] == 'BaseModel':
                    continue
                return schema

    def to_json(self) -> tp.Dict:
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
        return_s = self.get_get_handler()

        if self.method == 'get' and mod_s is not None:
            p[self.url][self.method]['responses'] = {'200': {'content': {'application/json': {'schema': mod_s}}}}
        else:
            if mod_s is not None and mod_s.get('title') != 'BaseModel':
                p[self.url][self.method]['requestBody'] = {'content': {'application/json': {'schema': mod_s}}}
            if return_s is not None:
                p[self.url][self.method]['responses'] = {'200': {'content': {'application/json': {'schema': return_s}}}}
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

    def get_models(self) -> tp.Sequence[BaseModel]:
        models = []
        for serverless_function in [serverless for serverless in self.handlers if isinstance(serverless, ServerlessFunction)]:
            models.extend(serverless_function.get_models())
        return models

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
