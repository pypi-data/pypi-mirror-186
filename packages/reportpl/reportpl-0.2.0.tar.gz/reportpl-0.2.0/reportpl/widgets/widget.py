from pathlib import Path
from typing import Any, IO,  Optional, Protocol, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from reportpl.base_web_form import BaseWebForm

from reportpl.types import ConverterType, ErrorsType, FileType, ValidatorType, WidgetAttributesType


class Widget(Protocol):

    validators: list[ValidatorType]
    converter: Optional[ConverterType]
    col: int
    name: str
    form: 'BaseWebForm'

    def get_default_data(self) -> Any:
        pass

    def convert_data(self, raw_data: Any) -> Tuple[Any, ErrorsType]:
        pass

    def get_layout(self) -> WidgetAttributesType:
        pass

    @staticmethod
    def save_widget_assets(widget_folder: Path, files: list[FileType]) -> Any:
        pass

    def get_update_data(self, payload: Any) -> Any:
        pass
