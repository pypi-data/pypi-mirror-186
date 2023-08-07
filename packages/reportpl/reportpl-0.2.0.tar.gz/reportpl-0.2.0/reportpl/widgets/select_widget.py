from pathlib import Path
from typing import Any, IO, Optional, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from reportpl.base_web_form import BaseWebForm

from reportpl.types import ConverterType, ErrorsType, FileType, ModelListItem, ValidatorType, WidgetAttributesType, ValidationError
import stringcase


class SelectWidget:

    def __init__(self, form: 'BaseWebForm',
                 name: str,
                 options: list[str] | list[ModelListItem] | str,
                 label: str | None = None,
                 col: int = 0,
                 default: str = "",
                 validators: list[ValidatorType] = [],
                 converter: Optional[ConverterType] = None) -> None:
        self.form = form
        self.name = name
        self.col = col
        self.default = default
        self.options = options
        self._options_obj: list[ModelListItem]|None = None
        self.label = label or stringcase.capitalcase(name)
        self.validators = validators
        self.converter = converter

    @staticmethod
    def save_widget_assets(widget_folder: Path, files: list[FileType]) -> Any:
        pass

    def get_update_data(self, payload: Any) -> Any:
        pass

    @property
    def options_obj(self)->list[ModelListItem]:
        if self._options_obj is None:
            if isinstance(self.options, str):
                self._options_obj = self.form.reportpl.get_list(self.options)
            else:
                self._options_obj = [self._convert_item_list(item) for item in self.options]
        if len(self._options_obj) == 0:
            raise Exception("There is no options defined")
        return self._options_obj

    def _convert_item_list(self, item) -> ModelListItem:
        if isinstance(item, str):
            return {'key': item, 'value': item}
        return item

    def convert_data(self, raw_data: Any) -> Tuple[Any, ErrorsType]:
        try:
            self.data = self.converter(self.form, raw_data['value']) if self.converter else raw_data['value']
        except ValidationError as e:
            return None, str(e)
        for v in self.validators:
            try:
                v(self.form, self.data)
            except ValidationError as e:
                return None, str(e)
        return self.data, None



    def get_layout(self) -> WidgetAttributesType:
        if isinstance(self.options, str):
            options = self.form.reportpl.get_list(self.options)
        else:
            options = [self._convert_item_list(item) for item in self.options]
        return {
            'field_name': self.name,
            'widget_type': "select_widget",
            'label': self.label,
            'col': self.col,
            'widget_props': {
                'options': options,
            }
        }

    def get_default_data(self) -> Any:
        for item in self.options_obj:
            if item['key'] == self.default:
                return item
        else:
            return self.options_obj[0]
