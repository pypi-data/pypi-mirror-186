from pathlib import Path
from typing import Any
from docxtpl.subdoc import Subdoc
from reportpl.module_model import ModuleModel
from docxtpl import DocxTemplate

def add_subdoc_from_template(tpl: DocxTemplate, template: str|Path, context: Any) -> Subdoc:
    path = Path(template)
    if not path.exists():
        raise FileNotFoundError(f"the template \"{path}\" was not found")
    subtpl = DocxTemplate(str(path))
    subtpl.render(context)
    sd: Subdoc = tpl.new_subdoc()
    sd.subdocx = subtpl.docx
    return sd
       

class SubdocFunction:
    def __init__(self, tpl: DocxTemplate, module_model: ModuleModel):
        self.tpl = tpl
        self.module_model = module_model

    def __call__(self, template, **kargs):
        # if not isinstance(context, dict):
        #     context = {'data': context}
        path = self.module_model.docx_templates_folder / template
        try:
            return add_subdoc_from_template(self.tpl, path, kargs)
        except FileNotFoundError:
            return 
        # if not path.exists():
        #     print(f"Não foi encontrado o arquivo {path}")
        #     return
        # subtpl = DocxTemplate(str(path))
        # subtpl.render(context)
        # sd: Subdoc = self.tpl.new_subdoc()
        # sd.subdocx = subtpl.docx
        # return sd
