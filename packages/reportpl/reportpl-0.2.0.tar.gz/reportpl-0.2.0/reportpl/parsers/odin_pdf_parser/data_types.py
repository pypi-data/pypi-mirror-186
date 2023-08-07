
class OdinParserDataPericia:
    def __init__(self) -> None:
        self.seq: int = 0
        self.rg: int = 0
        self.ano: int = 0

    def __repr__(self) -> str:
        return f"{self.seq}/{self.rg}/{self.ano}"

class OdinParserDataQusito:
    def __init__(self) -> None:
        self.numero: str = ""
        self.data_criacao: str = ""
        self.responsavel: str = ""
        self.unidade_origem: str = ""
        self.conteudo: str = ""


class OdinParserData:
    def __init__(self) -> None:
        self.pericia = OdinParserDataPericia()
        self.ocorrencia: str = ""
        self.data_ocorrencia: str = ""
        self.rai: str = ""
        self.unidade_solicitante: str = ""
        self.autoridade: str = ""
        self.quesito = OdinParserDataQusito()
        self.pessoas: list[str] = []
