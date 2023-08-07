from docxtpl.subdoc import Subdoc
from .paragraph import parse_paragraph
from .heading import parse_heading
# from .subdoc_docx import parse_subdoc_docx


def parse_element(doc: Subdoc, el):
    if el.name == "p":
        parse_paragraph(doc, el)
    elif el.name in ['h1', 'h2', 'h3', 'h4', 'h5']:
        parse_heading(doc, el)
    # elif el.name == "sub":
    #     parse_subdoc_docx(doc, el)
    else:
        raise Exception(f"Element of type \"{el.name}\" not implemented")
    