# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reportpl',
 'reportpl.api',
 'reportpl.api.database',
 'reportpl.doc_handler',
 'reportpl.doc_handler.subdoc',
 'reportpl.doc_handler.subdoc_html',
 'reportpl.doc_handler.subdoc_html.elment_parses',
 'reportpl.html_render',
 'reportpl.models_example',
 'reportpl.models_example.celular_sinf',
 'reportpl.models_example.celular_sinf.filters',
 'reportpl.models_example.celular_sinf.functions',
 'reportpl.models_example.celular_sinf.web_form',
 'reportpl.models_example.example',
 'reportpl.models_example.example.filters',
 'reportpl.models_example.example.functions',
 'reportpl.models_example.example.web_form',
 'reportpl.models_example.example2',
 'reportpl.models_example.example2.filters',
 'reportpl.models_example.example2.functions',
 'reportpl.models_example.example2.web_form',
 'reportpl.parsers',
 'reportpl.parsers.odin_pdf_parser',
 'reportpl.pics_analyzer',
 'reportpl.web_converters',
 'reportpl.web_validators',
 'reportpl.widgets']

package_data = \
{'': ['*'],
 'reportpl.api': ['static/front/*',
                  'static/front/css/*',
                  'static/front/js/*',
                  'templates/*'],
 'reportpl.models_example.celular_sinf': ['lists/*', 'templates/*'],
 'reportpl.models_example.example': ['lists/*', 'templates/*'],
 'reportpl.models_example.example2': ['html_templates/*',
                                      'lists/*',
                                      'templates/*']}

install_requires = \
['Flask>=2.1.2,<3.0.0',
 'Markdown>=3.3.7,<4.0.0',
 'Pillow>=9.1.0,<10.0.0',
 'SQLAlchemy>=1.4.36,<2.0.0',
 'beautifulsoup4',
 'docxtpl>=0.16.0,<0.17.0',
 'pdfminer-six>=20221105,<20221106',
 'stringcase>=1.2.0,<2.0.0']

setup_kwargs = {
    'name': 'reportpl',
    'version': '0.2.0',
    'description': '',
    'long_description': 'None',
    'author': 'renatormc',
    'author_email': 'renatomartinsrmc@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
