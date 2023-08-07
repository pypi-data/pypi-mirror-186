
from typing import Any, Type
from .types import ModelNotFoundError
from importlib.machinery import SourceFileLoader
from pathlib import Path
from reportpl.base_web_form import BaseWebForm
from reportpl.model_info import ModelInfo


class ModuleModel:
    def __init__(self, models_folder: str | Path, model_name: str) -> None:
        self.model_folder = Path(models_folder) / model_name
        self.model_name = model_name
        self.path = self.model_folder / "__init__.py"
        if not self.path.exists():
            raise ModelNotFoundError(f"Model \"{model_name}\" not found")
        self.module = SourceFileLoader(model_name, str(self.path)).load_module()

    def get_web_form(self) -> BaseWebForm:
        return self.module.web_form.Form()

    def get_model_meta(self) -> ModelInfo:
        return ModelInfo(self.model_folder)

    @property
    def docx_templates_folder(self) -> Path:
        return self.model_folder / "templates"

    @property
    def html_templates_folder(self) -> Path:
        return self.model_folder / "templates"

    @property
    def filters(self) -> Type:
        return self.module.filters.Filters

    @property
    def functions(self) -> Type:
        return self.module.functions.Functions

    @property
    def pre_html_file(self) -> Path:
        return self.model_folder / "pre.html"

    def pre(self, context: Any) -> None:
        self.module.pre.pre(context)
