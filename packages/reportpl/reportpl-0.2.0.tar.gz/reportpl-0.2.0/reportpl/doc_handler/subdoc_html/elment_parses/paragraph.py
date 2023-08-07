from docxtpl import Subdoc
from .utils import remove_extra_spaces
from bs4.element import Tag
from . run import add_run

def parse_paragraph(sd: Subdoc, el: Tag):
    p = sd.add_paragraph('')
    class_ = " ".join(el['class']) if el.has_attr('class') else "Normal"
    p.style = class_
    els = list(el.find_all("div", recursive=False))
    if len(els) > 0:
        for div in els:
            add_run(p, div)
    else:
        add_run(p, el)
    
        