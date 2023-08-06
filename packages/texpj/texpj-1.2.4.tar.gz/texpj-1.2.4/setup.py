# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['texpj']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0']

entry_points = \
{'console_scripts': ['texpj = texpj:main']}

setup_kwargs = {
    'name': 'texpj',
    'version': '1.2.4',
    'description': 'Utilidad para mantener plantillas de latex',
    'long_description': '# TexPj\n\nEs una forma sencilla para manejar plantillas de LaTeX.\n\n## Instalar plantilla con git\n\nSi es desde **Github** puede simplemente referirse a USUARIO/PROYECTO, en otro\ncaso active la bandera de url para clonar directamente desde el link.\n\n### Ejemplos\n\n```\ntexpj install BenyaminGaleano/report reporte "reportes para electrónica"\n```\n\n\n**Explicación:** texpj install recibe el Usuario y el nombre con el que se va a registrar\nen este caso se podrá hacer uso de la plantilla a través de **reporte**, y sólo funcionaría si el\nrepositorio pertenece a **Github**, la descripción es opcional.\n\n```\ntexpj install https://github.com/BenyaminGaleano/report.git "reportes para electrónica" reporte --url\n```\n\n**Explicación:** al igual que el anterior instala la plantilla con el nombre **reporte**, pero esta forma funciona con cualquier url compatible con git.\n\n\n## Comandos disponibles\n\n  * **add**      Registra DIRECTORY como una plantilla de latex y lo identifica...\n  * **create**   Crea una copia del template registrado como ALIAS en la posición...\n  * **install**  Instala el TEMPLATE de forma local y lo regitra como ALIAS.\n  * **launch**   Se encarga de abrir los archivos (primitivo).\n  * **list**     Lista todas las posibles plantillas guardadas.\n  * **remove**   Elimina la plantilla identificada como ALIAS, si es un enlace...\n  * **update**   Actualiza el template identificado con el ALIAS.\n  * **describe** cambiar la descripción de una plantilla.\n\n\n',
    'author': 'Benyamin Galeano',
    'author_email': 'benyamin.galeano@galileo.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
