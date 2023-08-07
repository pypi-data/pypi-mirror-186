from pathlib import Path
from typing import Any, IO, Callable, Optional, Tuple, TYPE_CHECKING
if TYPE_CHECKING:
    from reportpl.base_web_form import BaseWebForm
from reportpl.types import ConverterType, ErrorsType, FileType, ValidatorType, WidgetAttributesType, ValidationError
import stringcase


class FileWidget:

    def __init__(self, form: 'BaseWebForm',
                 name: str,
                 label: str | None = None,
                 col: int = 0, default="",
                 required: bool = False,
                 validators: list[ValidatorType] = [],
                 converter: Optional[ConverterType] = None,
                 file_parser: Optional[Callable[[Path], Any]] =None,
                 accept: str|None = None) -> None:
        self.form = form
        self.name = name
        self.col = col
        self.default = default
        self.required = required
        self.label = label or stringcase.capitalcase(name)
        self.validators = validators
        self.converter = converter
        self.file_parser = file_parser
        self.accept = accept

    @staticmethod
    def save_widget_assets(widget_folder: Path, files: list[FileType]) -> Any:
        try:
            widget_folder.mkdir(parents=True)
        except FileExistsError:
            pass
        files[0].save(widget_folder)
        return files[0].filename

    def get_update_data(self, payload: Any) -> Any:
        if self.file_parser is None:
            return {}
        path = self.form.reportpl.get_widget_assets_folder(self.name, create=True) / str(payload['relpath'])
        if path.exists():
            res = self.file_parser(path)
            return res or {}
        return {}

    def convert_data(self, raw_data: Any) -> Tuple[Any, ErrorsType]:
        text = str(raw_data).strip()
        if self.required and text == "":
            return None, "Campo obrigatório"
        data = self.form.reportpl.get_widget_assets_folder(self.name, create=True) / text
        print(data)
        if not data.exists():
            return None, "Campo obrigatório"
        try:
            self.data = self.converter(self.form, text) if self.converter else text
        except ValidationError as e:
            return None, str(e)
        for v in self.validators:
            try:
                v(self.form, self.data)
            except ValidationError as e:
                return None, str(e)
        return self.data, None

    def get_layout(self) -> WidgetAttributesType:
        return {
            'field_name': self.name,
            'widget_type': "file_widget",
            'label': self.label,
            'col': self.col,
            'widget_props': {'accept': self.accept},
        }

    def get_default_data(self) -> Any:
        return self.default
