# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deepl_fastapi']

package_data = \
{'': ['*']}

install_requires = \
['deepl-scraper-pp>=0.1.2,<0.2.0',
 'fastapi>=0.63.0,<0.64.0',
 'get-ppbrowser>=0.1.3,<0.2.0',
 'logzero>=1.6.3,<2.0.0',
 'nest-asyncio>=1.5.1,<2.0.0',
 'portalocker>=2.2.1,<3.0.0',
 'requests>=2.25.1,<3.0.0',
 'uvicorn>=0.13.4,<0.14.0']

entry_points = \
{'console_scripts': ['deepl-fastapi = deepl_fastapi.run_uvicorn:main']}

setup_kwargs = {
    'name': 'deepl-fastapi',
    'version': '0.1.2',
    'description': 'deepl via fastapi',
    'long_description': '# deepl-fastapi\n<!--- repo-name  pypi-name  mod_name func_name --->\n[![tests](https://github.com/ffreemt/deepl-fastapi/actions/workflows/routine-tests.yml/badge.svg)][![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/deepl-fastapi.svg)](https://badge.fury.io/py/deepl-fastapi)\n\nYour own deepl server via fastapi, cross-platform (Windows/Linux/MacOs) with API for OmegaT\n\n## Installation\n*   Create a virual environment: optional but recommended\n    e.g.,\n    ```bash\n    # Linux and friends\n    python3.7 -m venv .venv\n    source .venv/bin/activate\n\n    # Windows\n    # py -3.7 -m venv .venv\n    # .venv\\Scripts\\activate\n    ```\n\n```bash\npip install deepl-fastapi\n```\nor (if your use poetry)\n```bash\npoetry add deepl-fastapi\n```\nor\n```\n pip install git+https://github.com/ffreemt/deepl-fastapi.git\n```\nor\n*   Clone the repo [https://github.com/ffreemt/deepl-fastapi.git](https://github.com/ffreemt/deepl-fastapi.git)\n    ```bash\n    git clone https://github.com/ffreemt/deepl-fastapi.git\n    ```\n    and `cd deepl-fastapi`\n*   `pip install -r requirements.txt\n    * or ``poetry install``\n\n## Usage\n\n*   Start the server\n\nUse uvicorn directly (note the `deepl_server` module, not `run_uvicorn`)\n```bash\nuvicorn deepl_fastapi.deepl_server:app\n```\n\nor\n```bash\ndeepl-fastapi\n# this option is available only if installed via pip install or poetry add\n```\n\nor\n```bash\npython3.7 -m deepl_fastapi.run_uvicorn\n```\n\nor run the server on the external net, for example at port 9888\n```\nuvicorn deepl_fastapi.deepl_server:app --reload --host 0.0.0.0 --port 9888\n```\n\n*   Explore and consume\n\nPoint your browser to [http://127.0.0.1:8000/text/?q=test&to_lang=zh](http://127.0.0.1:8000/text/?q=test&to_lang=zh)\n\nOr in python code (`pip install requests` first)\n```python\nimport requests\n\n# get\nurl =  "http://127.0.0.1:8000/text/?q=test me&to_lang=zh"\nprint(requests.get(url).json())\n# {\'q\': \'test me\', \'from_lang\': None, \'to_lang\': \'zh\',\n# \'trtext\': \'考我 试探我 测试我 试探\'}\n\n# post\ntext = "test this and that"\ndata = {"text": text, "to_lang": "zh"}\nresp = requests.post("http://127.0.0.1:8000/text", json=data)\nprint(resp.json())\n# {\'q\': {\'text\': \'test this and that\', \'from_lang\': None, \'to_lang\': \'zh\', \'description\': None},\n# \'result\': \'试探 左右逢源 检验 审时度势\'}\n\n```\n\n## Interactive Docs (Swagger UI)\n\n [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)\n\n## OmegaT ``Fake MT`` plugin setup\n* Copy ``omegat-plugin-fake-mt-1.0.0.jar`` （available at https://github.com/briacp/omegat-plugin-fake-mt） to OmegaT\\plugins （e.g., C:\\Program Files\\OmegaT\\plugins） \n\nRun``OmegaT``and setup ``omegat-plugin-fake-mt``\n```bash\nOmegaT/Preferences/Machine Translation/Fake MT/Configure\n\tName: Fake Deepl MT\n\tURL: http://localhost:8000/text\n\tSource Parameter: from_lang\n\tTarget Parameter: to_lang\n\tText Parameter: q\n```\n![](img/plugin-setup.png)\n',
    'author': 'freemt',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ffreemt/deepl-fastapi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
