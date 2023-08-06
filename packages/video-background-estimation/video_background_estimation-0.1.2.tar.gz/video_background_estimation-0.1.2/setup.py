# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['video_background_estimation']

package_data = \
{'': ['*']}

install_requires = \
['opencv-python>=4.7.0.68,<5.0.0.0', 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'video-background-estimation',
    'version': '0.1.2',
    'description': 'background estimation based on simple techniques',
    'long_description': '# video_background_estimation\nRepo for background estimation from a video \n',
    'author': 'Rajesh Shreedhar Bhat',
    'author_email': 'rajeshbht19@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/rajesh-bhat/video_background_estimation',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
