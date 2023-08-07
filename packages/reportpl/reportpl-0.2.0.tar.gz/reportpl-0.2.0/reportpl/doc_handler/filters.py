from datetime import datetime
from .helpers_filters import *
import math
from pathlib import Path

nome_meses = [
    'janeiro',
    'fevereiro',
    'março',
    'abril',
    'maio',
    'junho',
    'julho',
    'agosto',
    'setembro',
    'outubro',
    'novembro',
    'dezembro'
]



class Filters:
    @staticmethod
    def br(value, loop_):
        return value if loop_.index == 1 else f"<w:br/>{value}"


    @staticmethod
    def not_null(value):
        if value is None:
            return ""
        return value

    @staticmethod
    def xxx(value):
        if value is None:
            return "XXX"
        return value

    @staticmethod
    def data_completa(value):
        if not isinstance(value, datetime):
            return ""
        dia = str(value.day).rjust(2, "0")
        dia_extenso = get_extenso(value.day)
        return f"{dia} ({dia_extenso}) dias do mês de {nome_meses[value.month - 1]} do ano de {value.year} ({get_extenso(value.year)})"

  
    @staticmethod
    def data_mes_extenso(value):
        if not isinstance(value, datetime):
            return ""
        dia = str(value.day) if value.day > 1 else f"{value.day}°"  
        return f"{dia} de {nome_meses[value.month - 1]} de {value.year}"
      

    @staticmethod
    def hora_minuto(value):
        if not isinstance(value, datetime):
            return "XXX"
        hora = str(value.hour).rjust(2, "0")
        minuto = str(value.minute).rjust(2, "0")
        return f"{hora}:{minuto}"

    @staticmethod
    def dia(value):
        if not isinstance(value, datetime):
            return "XXX"
        return str(value.day).rjust(2, "0")

    @staticmethod
    def dia_extenso(value):
        if not isinstance(value, datetime):
            return "XXX"
        dia = str(value.day).rjust(2, "0")
        dia_extenso = get_extenso(value.day)
        return f"{dia} ({dia_extenso})"

    @staticmethod
    def numero_extenso_masc(value):
        return get_extenso(value)

    @staticmethod
    def numero_extenso_fem(value):
        return get_extenso(value, feminino=True)

    @staticmethod
    def mes_extenso(value):
        if not isinstance(value, datetime):
            return "XXX"
        return nome_meses[value.month-1]

    @staticmethod
    def data_simples(value):
        if isinstance(value, datetime):
            return value.strftime("%d/%m/%Y")
        try:
            data = datetime.strptime(value, "%d/%m/%Y")
            return data.strftime("%d/%m/%Y")
        except Exception as e:
            print(e)
            pass

    @staticmethod
    def is_male(value):
        if isinstance(value, str):
            firstname = value.split()[0]
            return firstname.endswith('o')
        return False

    @staticmethod
    def get_extenso(value, feminino=False):
        return get_extenso(value, feminino=feminino)

    @staticmethod
    def datetime(value):
        try:
            return datetime.strptime(value, "%d/%m/%Y")
        except:
            pass

    @staticmethod
    def join_enumerate(values, with_quotes=False):
        n = len(values)
        if n == 0 :
            return ""
        if n == 1:
            return str(values[0])
        if with_quotes:
            values = [f"\"{v}\"" for v in values]
        else:
            values = [str(v) for v in values]
        parts1 = values[:-1]
        text1 = ", ".join(parts1)
        return f"{text1} e {values[-1]}"

    @staticmethod
    def moeda_extenso(value, prefix="R$ "):
        value_str = f"{value:.2f}".replace(".", ",")
        reais = math.floor(value)
        centavos = int((value%reais + 0.0000000001)*100) if reais > 0 else value*100
        reais_text = get_extenso(reais)
        aux1 = "reais" if reais > 1 else "real"
        aux2 = "centavos" if centavos > 1 else "centavo"
        centavos_text = get_extenso(centavos)
        
        middle_text = f"{reais_text} {aux1}"
        if centavos > 0:
            middle_text += f" e {centavos_text} {aux2}"
        text = f"{prefix}{value_str} ({middle_text})"
        return text

    @staticmethod
    def file_stem(value):
        try:
            path = Path(value)
            return path.stem
        except:
            return ""



filters = [getattr(Filters, func) for func in dir(Filters) if callable(
    getattr(Filters, func)) and not func.startswith("__")]
