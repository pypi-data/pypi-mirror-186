# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stauth']

package_data = \
{'': ['*']}

install_requires = \
['bcrypt>=4.0.1,<5.0.0',
 'extra-streamlit-components>=0.1.56,<0.2.0',
 'pyjwt>=2.6.0,<3.0.0',
 'streamlit>=1.16.0,<2.0.0']

setup_kwargs = {
    'name': 'stauth',
    'version': '0.1.4',
    'description': 'Basic Streamlit authenticator',
    'long_description': '# stauth\n\nStreamlit authentication components\n  \n## Installation\n\n```python\npip install stauth\n```\n',
    'author': 'Mysterious Ben',
    'author_email': 'datascience@tuta.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8, !=2.7.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*, !=3.7.*',
}


setup(**setup_kwargs)
