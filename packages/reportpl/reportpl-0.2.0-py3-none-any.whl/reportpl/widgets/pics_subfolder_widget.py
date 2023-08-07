import shutil
from typing import IO, Any, Optional, Tuple, TYPE_CHECKING, TypedDict
from reportpl.zipmodel import unzip_file
from pathlib import Path

if TYPE_CHECKING:
    from reportpl.base_web_form import BaseWebForm
from reportpl.types import ConverterType, ErrorsType, FileType, ValidatorType, WidgetAttributesType, ValidationError
import stringcase


class PicFolder(TypedDict):
    folder: str
    files: list[str]


class PicsSubfolderWidget:

    def __init__(self, form: 'BaseWebForm',
                 name: str,
                 label: str | None = None,
                 col: int = 0,
                 validators: list[ValidatorType] = [],
                 converter: Optional[ConverterType] = None) -> None:
        self.col = col
        self.form = form
        self.name = name
        self.label = label or stringcase.capitalcase(name)
        self.validators = validators
        self.converter = converter
        

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
        f = files[0]
        if f.filename.endswith(".zip"):
            f.save(folder)
        return f.filename

    def convert_data(self, raw_data: Any) -> Tuple[Any, ErrorsType]:
        filename = raw_data
        folder = self.form.reportpl.get_widget_assets_folder(
            self.name, create=True)
        zippath = folder / filename
        destfolder = folder / "extracted"
        try:
            shutil.rmtree(destfolder)
        except FileNotFoundError:
            pass
        destfolder = unzip_file(zippath, destfolder)

        data: list[PicFolder] = []
        for entry in destfolder.iterdir():
            if entry.is_dir():
                item: PicFolder = {"folder": entry.name, "files": []}
                for entry2 in entry.iterdir():
                    if entry2.is_file():
                        item['files'].append(str(entry2.absolute()))
                data.append(item)
        self.data = data

        for v in self.validators:
            try:
                v(self.form, self.data)
            except ValidationError as e:
                return None, str(e)
        return self.data, None

    def get_layout(self) -> WidgetAttributesType:
        return {
            'field_name': self.name,
            'widget_type': "pics_subfolder_widget",
            'label': self.label,
            'col': self.col,
            'widget_props': {},
        }

    def get_default_data(self) -> list[PicFolder]:
        return []
