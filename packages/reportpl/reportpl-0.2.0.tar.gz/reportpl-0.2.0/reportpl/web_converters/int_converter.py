from reportpl.types import ValidationError
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from reportpl.base_web_form import BaseWebForm


class IntConverter:
    def __init__(self, min: int|None = None, max: int|None = None) -> None:
        self.min = min
        self.max = max
    
    def __call__(self, form: 'BaseWebForm', value: str) -> int:
        try:
            val = int(value)
        except:
            raise ValidationError("Valor incorreto")
        if self.min and val < self.min:
            raise ValidationError(f"O valor precisa ser maior ou igual a {self.min}")
        if self.max and val > self.max:
            raise ValidationError(f"O valor precisa ser menor ou igual a {self.max}")
        return val