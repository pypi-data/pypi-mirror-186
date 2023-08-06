# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['brdata', 'brdata.cvm']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0',
 'beautifulsoup4>=4.10.0,<5.0.0',
 'cachier>=1.5.3,<2.0.0',
 'html5lib>=1.1,<2.0',
 'lxml>=4.6.4,<5.0.0',
 'pandas>=1.5.0,<2.0.0',
 'random-user-agent>=1.0.1,<2.0.0',
 'requests>=2.23.0,<3.0.0',
 'xlrd>=2.0.1,<3.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib_metadata>=4.5.0,<5.0.0']}

setup_kwargs = {
    'name': 'brasil-data',
    'version': '0.12.3',
    'description': 'Fontes de dados do mercado financeiro brasileiro',
    'long_description': '<p align="center">\n  <a href="https://github.com/gabrielguarisa/brdata"><img src="https://raw.githubusercontent.com/gabrielguarisa/brdata/0bd34000bf29bd5b93aee011f368bc0385680c58/logo.png?token=GHSAT0AAAAAABPPKYT7BQBOVDJG3NYYQKNOYQ5JIZA" alt="brdata"></a>\n</p>\n<p align="center">\n    <em>Fontes de dados do mercado financeiro brasileiro</em>\n</p>\n\n<div align="center">\n\n[![Package version](https://img.shields.io/pypi/v/brasil-data?color=%2334D058&label=pypi%20package)](https://pypi.org/project/brasil-data/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/gabrielguarisa/brdata/releases)\n[![License](https://img.shields.io/github/license/gabrielguarisa/brdata)](https://github.com/gabrielguarisa/brdata/blob/main/LICENSE)\n\n</div>\n\n## Instalação\n\n```shell\npip install brasil-data\n```\n\n## Utilização\n\n### XPI\n\nColetando dados da análise da XPI para uma determinada ação:\n\n```python\nfrom brdata import xpi\nxpi.analise("cyre3")\n```\n\n### Fundamentus\n\nColetando tabela do resultado da busca no Fundamentus (equivalenta a página https://www.fundamentus.com.br/resultado.php):\n\n```python\nfrom brdata import fundamentus\nfundamentus.resultados()\n```\n\nBalanços históricos de uma determinada ação:\n\n```python\nbalanco, demonstrativo = fundamentus.balanco_historico("mglu3")\n```\n\nDetalhes de uma ação:\n\n```python\nfundamentus.detalhes("mglu3")\n```\n\n### CVM\n\n\nImportando módulo:\n\n```python\nfrom brdata import cvm\n```\n\nBaixando os dados para um determinado tipo de prefixo:\n\n```python\ncvm.get_data(prefix)\n```\n\nObtendo os valores válidos para o parâmetro `prefix`:\n\n```python\ncvm.get_valid_prefixes()\n# [\'dfp\', \'fca\', \'fre\', \'ipe\', \'itr\']\n```\n\nConsumindo os valores dos formulários para cada um dos prefixos:\n\n```python\nr = cvm.Reader(prefix)\n```\n\nConsultando anos disponíveis de dados:\n\n```python\nr.years\n```\n\n#### Formulário Cadastral (FCA)\n\nUsando dados do [formulário cadastral](https://dados.gov.br/dataset/cia_aberta-doc-fca):\n\n```python\nfca = cvm.Reader("fca")\n```\n\nConsumindo dados históricos de uma determinada empresa num determinado formulário (`form_name`):\n\n```python\nfca.processors[form_name].get_cia_history("47.960.950/0001-21")\n```\n\nConsumindo os dados mais recentes para cada uma das empresas num determinado formulário (`form_name`):\n\n```python\nfca.processors[form_name].get_most_recent()\n```\n\nConsultando valores válidos para `form_name`:\n\n```python\nfca.forms\n```\n\n### B3\n\nImportando módulo:\n\n```python\nfrom brdata import b3\n```\n\nÍndices disponíveis:\n\n```python\nb3.indices()\n```\n\nColetando composição de um índice:\n\n```python\nb3.portfolio("ibov")\n```\n\nListando empresas disponíveis na B3:\n\n```python\nb3.cias()\n```\n\nListando todas as BDRs disponíveis:\n\n```python\nb3.bdrs()\n```\n\nDetalhamento de uma empresa:\n\n```python\nb3.detalhes(cvm_code="25135")\n```\n\n### Valor Econômico\n\nImportando módulo:\n\n```python\nfrom brdata import valor\n```\n\nPortfólios das instituições financeiras:\n\n```python\nvalor.portfolios(2, 2022)\n```\n\nCarteira Valor:\n\n```python\nvalor.carteira_valor(2, 2022)\n```\n\n## Contribuindo com o projeto\n\nPara contribuir com o projeto, consulte o [guia de contribuição](https://github.com/gabrielguarisa/brdata/blob/main/CONTRIBUTING.md).',
    'author': 'Gabriel Guarisa',
    'author_email': 'gabrielguarisa@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/gabrielguarisa/brdata',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
