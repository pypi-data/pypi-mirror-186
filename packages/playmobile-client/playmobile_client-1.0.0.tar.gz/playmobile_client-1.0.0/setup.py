# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['playmobile']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=22.0,<23.0',
 'faker>=16.6,<17.0',
 'httpx>=0.23,<0.24',
 'marshmallow>=3.18,<4.0']

setup_kwargs = {
    'name': 'playmobile-client',
    'version': '1.0.0',
    'description': 'Python client for Playmobile.uz API',
    'long_description': '# Python client for Playmobile.uz API (aka smsxabar.uz)\n\nThis is Python HTTP Client for [Playmobile.uz](https://playmobile.uz) (aka [smsxabar.uz](https://smsxabar.uz))\nbased on [httpx](https://github.com/encode/httpx).\n\nPlaymobile is a SMS broker which allows you to send messages throughout Uzbekistan.\n\n## Installation\n\nTo install playmobile-client, simply:\n\n``` bash\n$ pip install playmobile-client\n```\nThis package can be found on [PyPI](https://pypi.org/project/playmobile-client/).\n\n## Usage\n\n```python\nimport httpx\nimport playmobile\n\nclient = playmobile.HttpClient(\n    account=playmobile.Credentials(\n        username="example",\n        password="example",\n    ),\n    base_url=httpx.URL("https://playmobile-example.uz"),\n    session=httpx.Client(),\n)\n\nsms = playmobile.SMS(\n    id="unique_string",\n    sender="0001",\n    recipient="998xx3332211",\n    text="Hello world!",\n)\n\n# Single SMS\nclient.send_sms(sms)\n\n# SMS batch\nsms_batch = [\n    playmobile.SMS(\n        id="unique_string_1",\n        sender="0001",\n        recipient="998xx3332211",\n        text="Hello world!",\n    ),\n    playmobile.SMS(\n        id="unique_string_2",\n        sender="0001",\n        recipient="998xx3332211",\n        text="Yankee!",\n    ),\n]\nclient.send_sms_batch(sms_batch)  \n```\n\nYou can set up Timing settings:\n\n```python\nimport playmobile\n\nsms = playmobile.SMS(...)\n\ntiming = playmobile.Timing(\n    start_at=datetime(2023, 1, 1, 12, 0),\n    end_at=datetime(2023, 1, 1, 14, 0),\n)\n\n# Single SMS\nclient.send_sms(sms, timing=timing)\n```\n\nAdvanced users can set up HTTPX session with custom parameters. For example:\n\n```python\nclient = playmobile.Client(\n    ...,\n    session = httpx.Client(\n        timeout=httpx.Timeout(timeout=2.0),\n    ),\n)\n```\n\nPackage also have the test utils which will help you test your service:\n- playmobile.generate_sms\n- playmobile.generate_error\n',
    'author': 'Daniil Andreev',
    'author_email': 'dandreevv22@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/absolutionsuz/playmobile-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
