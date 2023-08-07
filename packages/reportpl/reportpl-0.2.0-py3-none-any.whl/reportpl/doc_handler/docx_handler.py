from pathlib import Path
from typing import Optional, Union
from docxtpl import DocxTemplate, InlineImage, Subdoc
from reportpl.doc_handler.jenv import make_jinja_env
from docx.shared import Mm
from uuid import uuid4
from reportpl.doc_handler.subdoc_html import SubdocHtmlFunction
from reportpl.module_model import ModuleModel
from reportpl.doc_handler.subdoc import SubdocFunction


class SInlineImage:
    def __init__(self, tpl):
        self.tpl = tpl

    def __call__(self, file, width):
        path = Path(file)
        if not path.exists():
            return
        return InlineImage(self.tpl, file, width=Mm(width))


class DocxHandler:
    def __init__(self, module_model: ModuleModel):
        self.module_model = module_model
        self.templates_folder = self.module_model.docx_templates_folder
        self.jinja_env = make_jinja_env(self.module_model)
        self.context = None
        self.pos_subdocs: list[Subdoc]  = []

    def prepare_jinja_env(self, tpl: DocxTemplate):
        self.jinja_env.globals['subdoc'] = SubdocFunction(tpl, self.module_model)
        jinja_env2 = make_jinja_env(self.module_model, self.module_model.html_templates_folder)
        self.jinja_env.globals['subdoc_html'] = SubdocHtmlFunction(self, tpl, self.module_model, jinja_env2)
        self.jinja_env.globals['image'] = SInlineImage(tpl)
        return self.jinja_env

    def render_temp(self, template, context):
        path = self.templates_folder / template
        if path.exists():
            tpl = DocxTemplate(str(path))
            jinja_env = self.make_jinja_env(tpl)
            tpl.render(context, jinja_env)
            tempfile = self.TEMPFOLDER / f"{uuid4()}.docx"
            tpl.save(tempfile)
            return tempfile

    def render(self, template: str, context, dest_file: Union[Path, str]) -> Optional[Path]:
        self.context = context
        dest_file = Path(dest_file)
        path = self.templates_folder / template
        if path.exists():
            tpl = DocxTemplate(str(path))
            jinja_env = self.prepare_jinja_env(tpl)
            tpl.render(context, jinja_env)
            tpl.save(dest_file)
      

            #Renderizar uma segunda vez para inserir os subdocs referenciados nos templates html
            # tpl = DocxTemplate(str(dest_file))
            # jinja_env = self.prepare_jinja_env(tpl)
            # subdocs: list[Subdoc] = []
            # for doc in self.pos_subdocs:
            #     sd: Subdoc = tpl.new_subdoc()
            #     sd.subdocx = doc.docx
            #     subdocs.append(sd)
            # tpl.render({'pos_subdocs': subdocs}, jinja_env)
            # tpl.save(dest_file)
            return dest_file
        return None
