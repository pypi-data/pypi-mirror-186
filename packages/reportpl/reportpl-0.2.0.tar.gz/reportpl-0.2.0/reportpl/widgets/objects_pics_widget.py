import shutil
from typing import IO, Any, Optional, Tuple, TYPE_CHECKING, TypedDict

from pathlib import Path

if TYPE_CHECKING:
    from reportpl.base_web_form import BaseWebForm
from reportpl.types import ConverterType, ErrorsType, FileType, ValidatorType, WidgetAttributesType, ValidationError
import stringcase


class PicData(TypedDict):
    path: str
    selected: bool


class ObjectData(TypedDict):
    name: str
    pics: list[PicData]


class ObjectsPicsWidget:

    def __init__(self, form: 'BaseWebForm',
                 name: str,
                 label: str | None = None,
                 col: int = 0,
                 validators: list[ValidatorType] = [],
                 converter: Optional[ConverterType] = None,
                 new_object_name: str = "Sem nome",
                 multiple=False) -> None:
        self.col = col
        self.form = form
        self.name = name
        self.multiple = multiple
        self.label = label or stringcase.capitalcase(name)
        self.new_object_name = new_object_name
        self.validators = validators
        self.converter = converter

    @staticmethod
    def get_data_from_folder(widget_folder: Path) -> Any:
        folder = widget_folder
        try:
            widget_folder.mkdir(parents=True)
        except FileExistsError:
            pass
        pics = [{'path': f"{entry.name}", 'selected': False}
                for entry in folder.iterdir() if entry.is_file()]
        pics.sort(key=lambda x: x['path'])  # type: ignore
        return [{'name': '0', 'pics': pics}]

    def get_update_data(self, payload: Any) -> Any:
        pass

    @staticmethod
    def save_widget_assets(widget_folder: Path, files: list[FileType]) -> Any:
        try:
            shutil.rmtree(widget_folder)
        except FileNotFoundError:
            pass
        folder = widget_folder
        folder.mkdir(parents=True)
        for f in files:
            if f.filename.endswith(".zip"):
                pass
            else:
                f.save(folder)
        return ObjectsPicsWidget.get_data_from_folder(widget_folder)

    def convert_data(self, raw_data: Any) -> Tuple[Any, ErrorsType]:
        data: list[ObjectData] = raw_data
        folder = self.form.reportpl.get_widget_assets_folder(
            self.name, create=True)
        for i, obj in enumerate(data):
            data[i]['pics'] = [{'path': str(
                folder / pic['path']), 'selected': pic['selected']} for pic in obj['pics']]
        try:
            self.data = self.converter(
                self.form, data) if self.converter else data
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
            'widget_type': "objects_pics_widget",
            'label': self.label,
            'col': self.col,
            'widget_props': {
                'new_object_name': self.new_object_name,
                'multiple': self.multiple
            },
        }

    def get_default_data(self) -> list[list[ObjectData]]:
        return self.get_data_from_folder(self.form.reportpl.get_widget_assets_folder(self.name))
