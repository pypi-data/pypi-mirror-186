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
    'version': '0.1.4',
    'description': 'background estimation based on simple techniques',
    'long_description': '# video_background_estimation\nBackground estimation of videos using simple technques. \n\n#### Input:\n![ezgif-5-41733c4472](https://user-images.githubusercontent.com/6439266/213073414-17089212-3016-4c09-8741-0bb585bc2003.gif)\n\n\n#### Output:\n![image](https://user-images.githubusercontent.com/6439266/213074235-668b7cb4-7f6f-40d4-909e-dc386c2e26af.png)\n\n\n#### Usage\n```\nfrom video_background_estimation.EstimateBackground import BackgroundEstimation\nback_est = BackgroundEstimation("videos/british_highway_traffic.mp4", frame_fraction=0.1)\nresult = back_est.get_background(method="median")\n```\n\n##### Acknowledgement:\nThanks to my colleague Dinesh Ladi for all the help with Poetry.\n\n##### References:\n[1] Road Traffic Video Monitoring. https://www.kaggle.com/datasets/493b50c9f4c536c08262acadfeca70e2e4df0dadacae1655e8669903b2e21623. <br>\n[2] Simple Background Estimation in Videos Using OpenCV (C++/Python) | LearnOpenCV #. 27 Aug. 2019, https://learnopencv.com/simple-background-estimation-in-videos-using-opencv-c-python/\n',
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
