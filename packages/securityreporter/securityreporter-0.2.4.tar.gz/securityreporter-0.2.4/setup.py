# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reporter', 'reporter.objects']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'securityreporter',
    'version': '0.2.4',
    'description': 'A Python wrapper for the Reporter API.',
    'long_description': 'python-reporter\n===============\n\n.. image:: https://github.com/dongit-org/python-reporter/workflows/test/badge.svg\n   :target: https://github.com/dongit-org/python-reporter/actions\n   :alt: Test Status\n\n.. image:: https://codecov.io/gh/dongit-org/python-reporter/branch/main/graph/badge.svg\n   :target: https://codecov.io/gh/dongit-org/python-reporter\n   :alt: Code Coverage\n\n.. image:: https://readthedocs.org/projects/python-reporter/badge/?version=latest\n   :target: https://python-reporter.readthedocs.io/en/latest/?badge=latest\n   :alt: Documentation Status\n\n.. image:: https://img.shields.io/pypi/v/securityreporter\n   :target: https://pypi.org/project/securityreporter/\n   :alt: PyPI\n\nA Python wrapper around the `Reporter <https://securityreporter.app>`_ API.\n\nCurrently compatible with Reporter version `2023.01.17 <https://securityreporter.app/releases/20230117>`_.\n\nInstallation\n------------\n\nCurrently, :code:`python-reporter` is compatible with Python 3.7+.\n\nUse :code:`pip` to install the package:\n\n.. code:: bash\n\n    pip install --upgrade securityreporter\n\nDocumentation\n-------------\n\nDocumentation is available on `Read the Docs <https://python-reporter.readthedocs.io/>`_.\n\nAbout Reporter\n---------------\n\n.. image:: https://raw.githubusercontent.com/dongit-org/python-reporter/main/docs/_static/reporter_logo.png\n   :target: https://securityreporter.app/\n   :alt: Reporter Logo\n\nReporter is an all-in-one pentest reporting workspace designed to help your team organize pentests, interact with clients, and create high quality pentest reports.\n\nReporter is designed to allow managers to delegate tasks to individual pentesters easily. The pentesters in turn are easily able to see which tasks are assigned, and they can access all required assessment details to get started.\n\nReporter supports granular access control distinctions, ensuring that every user only has access to that which they are required to have access to.\n\nWith Reporter clients may directly interact with researchers or other team members. After research findings are published, clients may ask questions regarding specific findings, or they may request retests.\n\nReporter has many functionalities, such as custom and built-in finding templates and automatic PDF generation, that will save you large amounts of time during your research.',
    'author': 'Alexander Krigsman',
    'author_email': 'alexander.krigsman@dongit.nl',
    'maintainer': 'Stefan van der Lugt',
    'maintainer_email': 'stefan.vanderlugt@dongit.nl',
    'url': 'https://securityreporter.app/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
