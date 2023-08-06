# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['caronte_common',
 'caronte_common.data',
 'caronte_common.interfaces',
 'caronte_common.types']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'caronte-api-common',
    'version': '0.2.0',
    'description': 'Common components and modules to integrate Caronte layers',
    'long_description': '### Caronte api common\n\nThe Caronte api Common is a part of four layers inspered by DDD (Domain drive design) methodology, this package is like the same as Application layer and have the same concepts. It has generic functionalities based on base project requirements and have an objective to share code throughout Caronte layers.\n\nNow you can use this modules:\n\n- data (At this module you can use the data transfer object classes)\n- interfaces (Here it has generic interfaces)\n- types (Type definition of project objects)\n',
    'author': 'Giovani Liskoski Zanini',
    'author_email': 'giovanilzanini@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
