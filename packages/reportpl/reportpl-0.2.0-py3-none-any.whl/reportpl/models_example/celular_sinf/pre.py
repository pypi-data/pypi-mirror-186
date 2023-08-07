import copy


def pre(context):
    context['peritos'] = copy.deepcopy(context['relatores'])
    if context['revisor']:
        context['peritos'].append(context['revisor'])
    context['n_objetos'] = len(context['objects']) - 1
    try:
        context['pics'] = context['objects'][0]['pics']
    except IndexError:
        context['pics'] = []
    context['objects'] = context['objects'][1:]