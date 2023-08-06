import jinja2
from conf.project import TEMPLATES_PATH, EXTENSIONS_PATH, GLOBAL_TEMPLATE_OBJECTS_PATH
import os
from typing import Callable, Type
from .extensions.base_extension import BaseExtension
import importlib
from litehttp.http.responses import HtmlResponse


class RenderTemplate:
    def __init__(self, template_path, request):
        self.template_path = template_path
        self._template_source: str = ''
        self._methods = []
        self.request = request

    def set_template_methods(self, functions: list[Callable]):
        self._methods = functions
        return self

    def render(self, **kwargs) -> str:
        try:
            for templ in TEMPLATES_PATH:
                filepath = os.path.join(templ, self.template_path)
                if os.path.exists(filepath):
                    return HtmlResponse(self.request).response(
                        _JinjaInit(filepath, self.request).template_methods(self._methods).jinit(**kwargs)
                    )
            # raise RenderTemplateNotFound('RenderTemplate.render')
            raise 'RenderTemplate.render'
        except Exception as e:
            raise e


class _JinjaInit:
    def __init__(self, filepath: str, request):
        self._path = filepath.split('templates')[-1]
        self.request = request
        self._env = jinja2.Environment(loader=self._get_loader(), extensions=self._get_extensons())
        self._template = self._env.get_template(self._path)
        self._template_obj = []

    def template_methods(self, methods: list[callable]):
        """
        Adding Python methods to all templates.
        """
        for meth in methods:
            methname = meth.__name__
            self._env.globals[methname] = meth
        return self

    def _get_loader(self) -> jinja2.ChoiceLoader:
        """
        Creates loaders for html templates.
        """
        try:
            fsl = []
            for template in TEMPLATES_PATH:
                fsl.append(jinja2.FileSystemLoader(template))
            loader = jinja2.ChoiceLoader(fsl)
            return loader
        except Exception as e:
            raise e

    def _get_extensons(self) -> list[Type[BaseExtension]]:
        """
        Collects all template extensions (Classes) inherited from BaseExtension.
        """
        import litehttp.http.templates.extensions.project_extensions
        for path in EXTENSIONS_PATH:
            p = path.replace('/', '.')
            importlib.import_module(f'{p}template_ext')
        self._set_extensions_request(BaseExtension.__subclasses__())
        return BaseExtension.__subclasses__()

    def _set_extensions_request(self, extensions: list[Type[BaseExtension]]):
        for ext in extensions:
            ext.set_request(self.request)

    def jinit(self, **kwargs):
        objects = kwargs
        global_t_path = (os.path.join(GLOBAL_TEMPLATE_OBJECTS_PATH, 'global_t_obj'))
        if os.path.exists(global_t_path+'.py'):
            global_t_obj = __import__(global_t_path.replace('/', '.'), fromlist=['objects'])
            objects = getattr(global_t_obj, 'objects')
            objects.update(kwargs)

        for obj in self._template_obj:
            kwargs[obj] = self._template_obj[obj]
        render = self._template.render(objects)
        return render
