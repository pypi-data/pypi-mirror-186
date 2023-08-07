# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyfeign']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'pyfeign',
    'version': '0.1.2',
    'description': 'Declarative Python HTTP Client, inspired by the OpenFeign java project',
    'long_description': '# PyFeign - Declarative REST Client\n\nPython implementation of Feign.\n\n## Installation\n\n```bash\npip install pyfeign\n# or\npoetry install pyfeign\n```\n\n## Usage\n\nDecorate function with appropriate `pyfeign.$method` decorator:\n\n```python\n@pyfeign.get(url=\'http://localhost/{id}\')\ndef get_by_id(id: str = Path()) -> Dict[str, Any]:\n    """\n    Get by ID\n    """\n\n\nobj_dict = get_by_id(\'id123\')\n```\n\n### Parameters\n\n* Path - Argument should be used as a path template variable. Reserved variable names can be used using the `name`\n  parameter:\n\n    ```python\n    @pyfeign.get(url=\'http://localhost/{id}\')\n    def get_by_id(id_val: str = Path(name=\'id\')) -> Dict[str, Any]:\n        """\n        Get by ID\n        """\n    ```\n\n* Query - Argument should be used as a query parameter, and can be optionally set with a default value if not provided\n\n    ```python\n    @pyfeign.get(url=\'http://localhost/{id}\')\n    def get_by_id(id_val: str = Path, \n                  summary: bool = Query(default=False, name=\'summary_details\')) -> Dict[str, Any]:\n        """\n        Get by ID\n  \n        get_byt_id(\'id1\', False) == http://localhost/id1?summary_details=False\n        """\n    ```\n\n* Header - Argument will be used as an HTTP Header\n\n* Cookie - Argument will be used as an HTTP Cookie\n\n* Body - Argument will be sent as the request body (JSON serialized)\n\n### Classes\n\n```python\n@pyfeign.Pyfeign(config=Config(base_url=\'https://postman-echo.com\'))\nclass PostmanEcho:\n    @pyfeign.get(\'/get\')\n    def get(self, foo1: str = Query(), foo2: str = Query(default=\'bar2\')) -> Dict[str, Any]:\n        pass\n```\n\n### Responses\n\nIf the response function / method is typed with `Dict` or `List`, then the response json will be parsed and returned.\n\nIf return type is `str` then the response text will be returned\n\nFor either of these responses, the return code is asserted via `Response.raise_for_status()`, and so an HTTPError will\nbe raised accordingly\n\nOtherwise the full `requests.Response` object is returned.',
    'author': 'Chris White',
    'author_email': 'chriswhite199@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/chriswhite199/pyfeign',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
