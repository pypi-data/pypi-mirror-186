from pathlib import Path
from typing import Any, IO, Optional, Tuple, TYPE_CHECKING
if TYPE_CHECKING:
    from reportpl.base_web_form import BaseWebForm
from reportpl.types import ConverterType, ErrorsType, FileType, ValidatorType, WidgetAttributesType, ValidationError
import stringcase


class TextAreaWidget:

    def __init__(self, form: 'BaseWebForm',
                 name: str,
                 label: str | None = None,
                 col: int = 0, default="",
                 placeholder: str = "",
                 required: bool = False,
                 validators: list[ValidatorType] = [],
                 converter: Optional[ConverterType] = None,
                 rows: int = 5) -> None:
        self.form = form
        self.name = name
        self.col = col
        self.default = default
        self.placeholder = placeholder
        self.required = required
        self.label = label or stringcase.capitalcase(name)
        self.validators = validators
        self.converter = converter
        self.rows = rows

    @staticmethod
    def save_widget_assets(widget_folder: Path, files: list[FileType]) -> Any:
        pass

    def get_update_data(self, payload: Any) -> Any:
        pass

    def convert_data(self, raw_data: Any) -> Tuple[Any, ErrorsType]:
        text = str(raw_data).strip()
        if self.required and text == "":
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
            'widget_type': "text_area_widget",
            'label': self.label,
            'col': self.col,
            'widget_props': {'placeholder': self.placeholder, 'rows': self.rows},
        }

    def get_default_data(self) -> Any:
        return self.default
