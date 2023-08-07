from typing import Any, Optional, Tuple
from reportpl.types import  ErrorsType
from reportpl.widgets import Widget


class CompositeWidget:

    def __init__(self, widgets: list[list[Widget]]) -> None:
        self.widgets = widgets

    def convert_data(self, raw_data: dict) -> Tuple[Any, ErrorsType]:
        context = {}
        errors: dict = {}
        for row in self.widgets:
            for w in row:
                try:
                    context[w.name], e = w.convert_data(raw_data[w.name])
                    if e is not None:
                        errors[w.name] = e
                except KeyError:
                    errors[w.name] = "missing field"
        e = errors if errors != {} else None
        return context, e


    def get_default_data(self) -> Any:
        data = {}
        for row in self.widgets:
            for w in row:
                data[w.name] = w.get_default_data()
        return data
