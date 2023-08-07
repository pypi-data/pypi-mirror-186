from pathlib import Path
from typing import IO, Any, Callable, TypedDict, TYPE_CHECKING
from shutil import copyfileobj

if TYPE_CHECKING:
    from reportpl.base_web_form import BaseWebForm


class ValidationError(Exception):
    pass


class ModelNotFoundError(Exception):
    pass


class ExternalBrigdWasNotSet(Exception):
    pass


class ModelListItem(TypedDict):
    key: str
    value: Any


class ModelList(TypedDict):
    name: str
    items: list[ModelListItem]


class InitialData:
    def __init__(self) -> None:
        self.context: dict = {}
        self.form_data: dict = {}


class WidgetAttributesType(TypedDict):
    field_name: str
    widget_type: str
    widget_props: Any
    label: str
    col: int


WidgetMatrixType = list[list[WidgetAttributesType]]

ValidatorType = Callable[['BaseWebForm', Any], None]

ConverterType = Callable[['BaseWebForm', Any], Any]
ErrorsType = dict[str, str] | str | list[str] | None
# FormDataType = dict[str, Any]


class ObjectType:
    def __init__(self,  type: str = "", pics: list[str] = [], name: str = "Sem nome") -> None:
        self.type: str = type
        self.pics: list[str] = pics
        self.name: str = name

    def pics_iterator(self):
        for pic in self.pics:
            yield Path(pic)

    def to_dict(self) -> dict[str, Any]:
        return {
            'type': self.type,
            'pics': self.pics,
            'name': self.name
        }

    def from_dict(self, data: dict[str, Any]) -> 'ObjectType':
        try:
            self.type = data['type']
        except KeyError:
            self.type = ""
        self.name = data['name']
        self.pics = data['pics']
        return self

    def __str__(self) -> str:
        text = f"type: {self.type}, name: {self.name}"
        for pic in self.pics:
            text += f"\n{pic}"
        return text


class CaseObjectsType:
    def __init__(self, folder: str | Path, objects: list[ObjectType] = [],
                 pics_not_classified: list[str] = [],
                 alias: str = "") -> None:
        self.folder: Path = Path(folder)
        self.objects: list[ObjectType] = objects
        self.pics_not_classified: list[str] = pics_not_classified
        self.alias: str = alias

    def pics_not_classified_iterator(self):
        for pic in self.pics_not_classified:
            yield Path(pic)

    def to_dict(self) -> dict[str, Any]:
        return {
            'objects': [obj.to_dict() for obj in self.objects],
            'pics_not_classified': self.pics_not_classified,
            'alias': self.alias
        }

    def from_dict(self, data: dict[str, Any]) -> 'CaseObjectsType':
        # self.folder = Path(data['folder'])
        self.objects = [ObjectType().from_dict(item)
                        for item in data['objects']]
        self.pics_not_classified = data['pics_not_classified']
        try:
            self.alias = data['alias']
        except KeyError:
            self.alias = ""
        return self

    def __str__(self) -> str:
        return (f"alias: {self.alias}, n_objetos: {len(self.objects)}, n_pics_not_classified: {len(self.pics_not_classified)}, folder: {self.folder}")


class ModelMetaType(TypedDict):
    full_name: str
    has_qt_form: bool
    has_web_form: bool


class FileType:
    def __init__(self, file: IO[bytes], filename: str) -> None:
        self.file = file
        self.filename = filename

    def save(self, destdir: str | Path, buffer_size: int = 0) -> None:
        path = Path(destdir) / self.filename
        with path.open("wb") as fd:
            copyfileobj(self.file, fd, buffer_size)
