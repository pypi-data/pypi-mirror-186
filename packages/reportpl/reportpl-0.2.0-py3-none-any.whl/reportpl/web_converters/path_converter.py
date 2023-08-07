from pathlib import Path
from typing import Literal
from reportpl.types import ValidationError
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from reportpl.base_web_form import BaseWebForm

class PathConverter:
    def __init__(self, type_:Literal['dir', 'file'] = 'file') -> None:
        self.type_ =  type_
    
    def __call__(self, form: 'BaseWebForm', value: str) -> Path|None:
        text = str(value).strip()
        if text == "":
            return None
        path = Path(text)
        if not path.exists():
            raise ValidationError("Caminho inexistente")
        if self.type_ == 'file' and not path.is_file():
            raise ValidationError("O endereço não é um endereço de arquivo válido")
        if self.type_ == 'dir' and not path.is_dir():
            raise ValidationError("O endereçõ não é um endereço de diretório válido")
        return path