from reportpl.types import ValidationError
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from reportpl.base_web_form import BaseWebForm

class FloatConverter:
    def __init__(self, decimal_separator=",", min: float|None = None, max: float|None = None) -> None:
        self.decimal_separator = decimal_separator
        self.min = min
        self.max = max

    def __call__(self, form: 'BaseWebForm', value: str) -> float:
        try:
            val = float(value.replace(",", "."))
        except:
            raise ValidationError("Valor incorreto")
        if self.min and val < self.min:
            raise ValidationError(f"O valor precisa ser maior ou igual a {str(self.min).replace(',', '.')}")
        if self.max and val > self.max:
            raise ValidationError(f"O valor precisa ser menor ou igual a {str(self.max).replace(',', '.')}")
        return val