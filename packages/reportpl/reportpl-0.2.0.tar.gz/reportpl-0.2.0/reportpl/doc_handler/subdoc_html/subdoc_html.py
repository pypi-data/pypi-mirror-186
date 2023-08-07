from typing import Any, TYPE_CHECKING
from bs4 import BeautifulSoup
from docxtpl import DocxTemplate, Subdoc
import jinja2
from reportpl.module_model import ModuleModel
from .elment_parses import parse_element
from uuid import uuid4

if TYPE_CHECKING:
    from reportpl.doc_handler import DocxHandler


class SubdocDocxFunction:
    def __init__(self, docx_handler: 'DocxHandler', tpl: DocxTemplate) -> None:
       self.docx_handler = docx_handler
       self.tpl = tpl

    def __call__(self, template, **context):
        n = len(self.docx_handler.pos_subdocs)
        path = self.docx_handler.module_model.docx_templates_folder / template
        subtpl = DocxTemplate(path)
        subtpl.render(context)
        # sd: Subdoc = self.tpl.new_subdoc()
        # sd.subdocx = subtpl.docx
        self.docx_handler.pos_subdocs.append(subtpl)
        return "{{p " + f"pos_subdocs[{n}]" + " }}"


class SubdocHtmlFunction:
    def __init__(self, docx_handler: 'DocxHandler', tpl: DocxTemplate, module_model: ModuleModel, jinja_env: jinja2.Environment):
        self.tpl = tpl
        self.module_model = module_model
        self.jinja_env = jinja_env
        self.jinja_env.globals['subdoc_docx'] = SubdocDocxFunction(docx_handler, tpl)
        self.docx_handler = docx_handler


    def __call__(self, template: str, context: Any = None) -> Subdoc:
        if not isinstance(context, dict):
            context = {'data': context}
        sd = self.tpl.new_subdoc()
        path = self.module_model.html_templates_folder / template
        if not path.exists():
            raise FileNotFoundError(f"the template \"{path}\" was not found")
        tp = self.jinja_env.get_template(template)
        text = tp.render(ctx=self.docx_handler.context, **context)
        soup = BeautifulSoup(text, 'html.parser')
        for e in soup.find_all(recursive=False):
            parse_element(sd, e)
        return sd
