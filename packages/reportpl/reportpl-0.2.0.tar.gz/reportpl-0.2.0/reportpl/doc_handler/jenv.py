from pathlib import Path
import jinja2

from reportpl.module_model import ModuleModel
from .filters import filters
from .jinja_env_functions import global_functions


def make_jinja_env(module_model: ModuleModel, folder_templates: str | Path | None = None) -> jinja2.Environment:
    Filters = module_model.filters
    custom_filters = [getattr(Filters, func) for func in dir(Filters)
                      if callable(getattr(Filters, func)) and not func.startswith("__")]
    Functions = module_model.functions
    custom_functions = [getattr(Functions, func) for func in dir(Functions)
                        if callable(getattr(Functions, func)) and not func.startswith("__")]
    if folder_templates is not None:
        jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(folder_templates))
    else:
        jinja_env = jinja2.Environment()
    for filter_ in filters:
        jinja_env.filters[filter_.__name__] = filter_
    for function_ in global_functions:
        jinja_env.globals[function_.__name__] = function_
    for filter_ in custom_filters:
        jinja_env.filters[filter_.__name__] = filter_
    for function_ in custom_functions:
        jinja_env.globals[function_.__name__] = function_
    return jinja_env
