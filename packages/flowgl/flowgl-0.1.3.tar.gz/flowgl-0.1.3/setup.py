# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flowgl']

package_data = \
{'': ['*']}

install_requires = \
['requests-toolbelt>=0.10.1,<0.11.0']

setup_kwargs = {
    'name': 'flowgl',
    'version': '0.1.3',
    'description': 'Flow Immersive python client for datasets API',
    'long_description': '# Flow Immersive Python Client\n\nAn easy way to push data from pandas to Flow.\n\n## Usage\n\nPush data to Flow, identifying the dataset with a title. \nPushing a new dataset with the same title will create a new dataset version.\n\n```python\nimport pandas as pd\n\n# Example pandas dataframe\ndf = pd.DataFrame({\n    \'name\': [\'John\', \'Jane\', \'Joe\'],\n    \'age\': [30, 25, 40],\n    \'city\': [\'New York\', \'San Francisco\', \'Los Angeles\']\n})\n\nfrom flowgl import Client\n\n# Import the client and create an instance with your credentials\nclient = Client(\n    username=...,\n    password=...,\n)\n\n# Push the dataframe to Flow by title\nclient.push_data(\n    df,\n    dataset_title=\'My Dataset\',\n)\n```\n\n## Development\n\n### Installation\n\nFirst, install python and poetry. If on Windows, ensure you add poetry\'s bin directory to your PATH environment variable (search for "environment variables" in the start menu).\n\nThen, clone the repository and step into it.\n```bash\ngit clone git@bitbucket.org:flowvr/flow-scripts.git\ncd flow-scripts\n```\n#### Create Virtual Environment\n\nCreate a virtual environment (replace python with python3 or py as per your installation).\n\n```bash\npython -m venv venv\n```\n\n#### Activate Virtual Environment\n\nThis will activate the virtual environment for the current terminal session. You should see (venv) at the start of your terminal prompt.\n\nOn Windows Powershell:\n```powershell\nSet-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force\n.\\venv\\Scripts\\Activate.ps1\n```\n\nOn Windows Command Prompt:\n```cmd\n.\\venv\\Scripts\\activate.bat\n```\n\nOn Mac/Linux/WSL:\n```bash\nsource venv/bin/activate\n```\n\n#### Install Dependencies\n\nFinally, install the dependencies with poetry.\n\n```bash\npoetry install\n```\n\n### Publishing\n\nTo publish a new version of the package, first update the version number in `pyproject.toml`.  \nThen, run the following commands: \n\n```bash\npoetry build\npoetry publish\n```\n',
    'author': 'Flow Immersive',
    'author_email': 'info@flow.gl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
