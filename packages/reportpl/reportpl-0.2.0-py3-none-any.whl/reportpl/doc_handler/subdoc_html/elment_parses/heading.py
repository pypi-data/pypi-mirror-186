from docxtpl import Subdoc
from .utils import remove_extra_spaces
from bs4.element import Tag
from .paragraph import parse_paragraph

def parse_heading(sd: Subdoc, el: Tag):   
    level = int(el.name[1:])
    # p = sd.add_paragraph(remove_extra_spaces(el.text))
    # p.style = f"Título {level}"
    # print(level)
    sd.add_heading(remove_extra_spaces(el.text), level=level)



   
        