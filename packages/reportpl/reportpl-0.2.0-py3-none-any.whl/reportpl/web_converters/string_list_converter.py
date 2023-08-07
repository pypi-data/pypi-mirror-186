from reportpl.types import ValidationError
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from reportpl.base_web_form import BaseWebForm


class StringListConverter:
    def __init__(self, sep=",") -> None:
        self.sep = sep
    
    def __call__(self, form: 'BaseWebForm', value: str) -> list[str]:
        if not value:
            return []
        return [p.strip() for p in value.split(self.sep)]