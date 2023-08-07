from datetime import datetime
from reportpl.types import ValidationError
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from reportpl.base_web_form import BaseWebForm

class DateConverter:
    def __init__(self, format="%d/%m/%Y") -> None:
        self.format = format

    def __call__(self, form: 'BaseWebForm', value: str) -> datetime:
        try:
            return datetime.strptime(value, self.format)
        except:
            raise ValidationError("Data inválida")