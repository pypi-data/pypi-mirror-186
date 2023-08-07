from typing import  Type
from .widget import Widget
from .text_widget import TextWidget
from .array_widget import ArrayWidget
from .checkbox_widget import CheckBoxWidget
from .select_widget import SelectWidget
from .text_area_widget import TextAreaWidget
from .typeahead_obj_widget import TypeAheadObjWidget
from .typeahead_widget import TypeAheadWidget
from .objects_pics_widget import ObjectsPicsWidget
from .file_widget import FileWidget
from .pics_subfolder_widget import PicsSubfolderWidget

__widgets__: dict[str, Type['Widget']] = {
    'text_widget': TextWidget,
    'array_widget': ArrayWidget,
    'checkbox_widget': CheckBoxWidget,
    'select_widget': SelectWidget,
    'text_widget': TextAreaWidget,
    'type_ahead_object_widget': TypeAheadObjWidget,
    'objects_pics_widget': ObjectsPicsWidget,
    'type_ahead_widget': TypeAheadWidget,
    'file_widget': FileWidget,
    'pics_subfolder_widget': PicsSubfolderWidget,
}


class WidgetNotFoundError(Exception):
    pass

def get_widget_class_by_widget_type(widget_type: str ) -> Type[Widget]:
    try:
        return __widgets__[widget_type]
    except KeyError:
        raise WidgetNotFoundError(f"widget of type \"{widget_type}\" was not found")

