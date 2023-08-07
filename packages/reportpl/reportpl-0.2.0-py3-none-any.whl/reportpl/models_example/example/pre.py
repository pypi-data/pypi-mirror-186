def pre(context):
    """Função que será executada antes da passagem do contexto para
    o template. Aqui é possível modificar o contexto. Converter variáveis,
    adicionar novas variáveis, etc."""
    context['nova_variavel'] = "Teste"