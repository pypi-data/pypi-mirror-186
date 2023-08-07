from pathlib import Path
from reportpl.widgets import TextWidget, ArrayWidget, TextAreaWidget, TypeAheadObjWidget, TypeAheadWidget, SelectWidget, CheckBoxWidget, ObjectsPicsWidget, FileWidget
from reportpl.types import ValidationError
from reportpl.web_converters import DateConverter, FloatConverter
from reportpl.base_web_form import BaseWebForm


class Form(BaseWebForm):


    @staticmethod
    def file_parse(path: Path):
        return {'nome': "Mudar nome"}

    def define_widgets(self):
        self.widgets = [
            [
                TextWidget(self, 'nome', default="", placeholder="Digite seu nome",required=True),
                TextWidget(self, 'date', label="Data",converter=DateConverter()),
                TextWidget(self, 'float_value', label="Valor flutuante",converter=FloatConverter()),
            ],
            [
                ArrayWidget(self, "pessoas", widgets=[
                    [
                        TextWidget(self, 'nome', default="Nome default", placeholder="Digite seu nome",required=True),
                        TextWidget(self, 'profissao', label="Profissão",required=True),
                    ]
                ])
            ],
            [
                TextAreaWidget(self, 'texto_long',label='Texto longo', rows=10)
            ],
            [
                TypeAheadObjWidget(self, 'test_typeahead_obj', options='cidades', label='TypeaheadObjWidget'),
                SelectWidget(self, 'test_select', options='cidades', default="Goiânia", label="Test Select"),
                CheckBoxWidget(self, 'test_checkbox', label="Test Checkbox", default=True)
            ]   ,
            [
                TypeAheadWidget(self, 'test_typeahead', options=['Goiania', "Patrocinio", ], label='TypeaheadWidget', default="Valor default"),
            ]   ,
            [
                ObjectsPicsWidget(self, 'fotos', label='Fotos', multiple=True),
            ]   
        ]