from reportpl.types import ValidationError
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from reportpl.base_web_form import BaseWebForm

class CpfConverter:
    def __init__(self) -> None:
       pass

    def __call__(self, form: 'BaseWebForm', value: str) -> str:
        cpf = [int(char) for char in value if char.isdigit()]
        if len(cpf) != 11 or cpf == cpf[::-1]:
            raise ValidationError("CPF inválido")
        for i in range(9, 11):
            aux = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
            digit = ((aux * 10) % 11) % 10
            if digit != cpf[i]:
                raise ValidationError("CPF inválido")
        return f"{cpf[:2]}.{cpf[3:5]}.{cpf[6:8]}-{cpf[9:10]}"        
