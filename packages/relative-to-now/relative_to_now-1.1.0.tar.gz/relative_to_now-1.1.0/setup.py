# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['RelativeToNow']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'relative-to-now',
    'version': '1.1.0',
    'description': "Print a datetime's distance from now",
    'long_description': '\n<h1 align="center">Relative To Now</h1>\n\n<h4 align="center">Convert date/time into a string relative to now.</h4>\n\n<p align="center">\n  <a href="https://pypi.org/project/relative-to-now/">\n    <img src="https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9-blue" alt="Python Version">\n  </a>\n  <a href="https://codecov.io/gh/Riverside-Healthcare/RelativeToNow">\n    <img src="https://codecov.io/gh/Riverside-Healthcare/RelativeToNow/branch/master/graph/badge.svg?token=PHYGI9FI22" alt="Codecov Status">\n  </a>\n  <a href="https://www.codacy.com/gh/Riverside-Healthcare/RelativeToNow/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Riverside-Healthcare/RelativeToNow&amp;utm_campaign=Badge_Grade">\n    <img src="https://app.codacy.com/project/badge/Grade/2533c8838ffe4c6a82c889d6d98f2050" alt="Codacy Status">\n  </a>\n  <a href="https://pypi.org/project/relative-to-now/">\n    <img src="https://badgen.net/pypi/v/relative-to-now" alt="Pypi Download">\n  </a>\n  <a href="https://pepy.tech/project/relative-to-now">\n    <img src="https://static.pepy.tech/badge/relative-to-now" alt="Downloads">\n  </a>\n</p>\n\n\n## 💾 Install\n\n```sh\npython -m pip install relative-to-now\n\n# or\n\npoetry add relative-to-now\n```\n\n## ✨ How to Use\n\nPossible input types:\n\n  * time.time()\n  * datetime.date.today()\n  * datetime.datetime.now()\n\nOptional inputs:\n\n  * ``no_errors`` (Defaults to ``False``, set to ``True`` to return value when there is an error instead of raising)\n\nOutput:\n    <int> <unit> <text>\n\nExamples:\n```python\nimport datetime\nfrom RelativeToNow import relative_to_now\n\nprint(relative_to_now(datetime.datetime.now() + datetime.timedelta(days=1)))\n>>> 1 day from now\n```\n\nPrecision for `datetime.date` is days.\n```python\nimport datetime\nfrom RelativeToNow import relative_to_now\n\nprint(relative_to_now(datetime.date.today() - datetime.timedelta(days=2)))\n>>> 2 days ago\n```\n\n```python\nimport time\nfrom RelativeToNow import relative_to_now\n\nprint(relative_to_now(time.time()))\n>>> just now\n```\n',
    'author': 'Christopher Pickering',
    'author_email': 'cpickering@rhc.net',
    'maintainer': 'Christopher Pickering',
    'maintainer_email': 'cpickering@rhc.net',
    'url': 'https://github.com/Riverside-Healthcare/RelativeToNow',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
