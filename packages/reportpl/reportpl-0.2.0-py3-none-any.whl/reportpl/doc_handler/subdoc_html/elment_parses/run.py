from .utils import remove_extra_spaces
from bs4.element import Tag

def add_run(p, el: Tag):
    r = p.add_run(remove_extra_spaces(el.text))
    if el.has_attr('bold'):
        r.bold = True
    if el.has_attr('italic'):
        r.italic = True
    if el.has_attr('underline'):
        r.underline = True
   