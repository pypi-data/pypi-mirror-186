from reportpl.converters import str2date


def get_context():
    return {
        "nome": "Renato Martins Costa",
        "idade": 38,
        "profissao": "Perito Criminal",
        "data_nascimento": str2date("30/08/1984")
    }
