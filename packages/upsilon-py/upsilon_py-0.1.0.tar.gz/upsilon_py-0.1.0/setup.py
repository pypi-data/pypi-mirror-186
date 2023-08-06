# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['upsilon_py']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'upsilon-py',
    'version': '0.1.0',
    'description': 'Connect to NumWorks calculators using Python',
    'long_description': '# Upsilon.py\n\nUpsilon.py is a wrapper for [upsilon.js]. It allow controlling the NumWorks from\nPython. To use this library, because of the dependency on Upsilon.js, you will\nneed a working installation of [Node] with [Npm]\n\n## Installation\n\nTo install Upsilon.py, you can use pip:\n\n```bash\npython3 -m pip install upsilon.py\n```\n\nAfter the installation, you will have to install Upsilon.js and its\ndependencies:\n\n```bash\nnpm install -g "upsilon.js@^1.4.1" usb\n```\n\n## Usage\n\nTo use Upsilon.py, you will need to import it:\n\n```python\nimport upsilon_py\n```\n\nThen, you can create a new NumWorks object:\n\n```python\nnumworks = upsilon_py.NumWorks()\n```\n\nYou will then be able to start the object and connect to the NumWorks:\n\n```python\nawait numworks.start()\nawait numworks.connect()\n```\n\nNow, the connection is established, you can send commands to the NumWorks:\n\n```python\n# Get the status of the NumWorks (connected/disconnected)\nstatus = await numworks.status()\nprint("Status:", status)\n\n# Get the model of the NumWorks (return 100/110/120)\nmodel = await numworks.get_model()\nprint("Model:", model)\n\n# Get the platform info of the NumWorks (information about the OS)\nplatform_info = await numworks.get_platform_info()\nprint("Platform info:", platform_info)\n\n# Backup the storage of the NumWorks\nstorage = await numworks.backup_storage()\n\n# Add a file to the storage\nstorage["records"].append({\n    "name": "Test",\n    "type": "py",\n    "autoImport": True,\n    "code": "print(\\"Hello World!\\")"\n})\n\n# Install the modified storage\nawait numworks.install_storage(storage)\n\n# Stop the object (you can also use numworks.disconnect() to keep the object\n# running and connect to another NumWorks)\nawait numworks.stop()\n```\n\n\n\n[upsilon.js]: https://www.npmjs.com/package/upsilon.js\n[Node]: https://nodejs.org/en/\n[Npm]: https://www.npmjs.com/\n',
    'author': 'Yaya-Cout',
    'author_email': 'yaya.cout@free.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
