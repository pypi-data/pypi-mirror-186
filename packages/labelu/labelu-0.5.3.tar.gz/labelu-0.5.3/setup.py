# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['labelu',
 'labelu.internal',
 'labelu.internal.adapter',
 'labelu.internal.adapter.persistence',
 'labelu.internal.adapter.routers',
 'labelu.internal.application',
 'labelu.internal.application.command',
 'labelu.internal.application.response',
 'labelu.internal.application.service',
 'labelu.internal.common',
 'labelu.internal.dependencies',
 'labelu.internal.domain.models',
 'labelu.internal.middleware',
 'labelu.internal.statics',
 'labelu.tests',
 'labelu.tests.internal',
 'labelu.tests.internal.adapter',
 'labelu.tests.internal.adapter.persistence',
 'labelu.tests.internal.adapter.routers',
 'labelu.tests.internal.common',
 'labelu.tests.utils']

package_data = \
{'': ['*'],
 'labelu.internal.statics': ['src/icons/*',
                             'src/img/example/*',
                             'static/css/*',
                             'static/js/*',
                             'static/media/*'],
 'labelu.tests': ['data/*']}

install_requires = \
['aiofiles>=22.1.0,<23.0.0',
 'appdirs>=1.4.4,<2.0.0',
 'email-validator>=1.3.0,<2.0.0',
 'fastapi>=0.86.0,<0.87.0',
 'loguru>=0.6.0,<0.7.0',
 'passlib[bcrypt]>=1.7.4,<2.0.0',
 'pillow>=9.3.0,<10.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'python-jose[cryptography]>=3.3.0,<4.0.0',
 'python-multipart>=0.0.5,<0.0.6',
 'sqlalchemy>=1.4.43,<2.0.0',
 'typer[all]>=0.7.0,<0.8.0',
 'uvicorn>=0.19.0,<0.20.0']

entry_points = \
{'console_scripts': ['labelu = labelu.main:cli']}

setup_kwargs = {
    'name': 'labelu',
    'version': '0.5.3',
    'description': '',
    'long_description': '<div align="center">\n<article style="display: flex; flex-direction: column; align-items: center; justify-content: center;">\n    <p align="center"><img width="300" src="https://user-images.githubusercontent.com/25022954/209616423-9ab056be-5d62-4eeb-b91d-3b20f64cfcf8.svg" /></p>\n    <h1 style="width: 100%; text-align: center;"></h1>\n    </p>\n</article>\n\n<a href="./README_zh-CN.md" >简体中文</a> | English\n\n\n</div>\n\n## Introduction\n\nLabelU is an open source data annotation tool that supports Chinese. At present, it has image annotation capabilities such as rectangle, polygon, point, line, classification, description. It can support detection, classification, segmentation, text transcription, Line detection, key point detection and other computer vision task scenarios. You can customize the annotation task by freely combining tools, and support COCO and MASK format data export.\n\n## Getting started\n\n### Download and Install miniconda\n\nhttps://docs.conda.io/en/latest/miniconda.html\n\n### Create virtual environment(python = 3.10)\n\n```bash\nconda create -n labelu python=3.10\n```\n\n### Activate virtual environment\n\n```bash\nconda activate labelu\n```\n\n### Install labelu\n\n```bash\npip install labelu\n```\n\n### Start labelu，server：http://localhost:8000\n\n```bash\nlabelu\n```\n\n## feature\n\n- Uniform，Six image annotation tools are provided, which can be configured through simple visualization or Yaml\n- Unlimited，Multiple tools can be freely combined to meet most image annotation requirements\n\n<p align="center">\n<img style="width: 600px" src="https://user-images.githubusercontent.com/25022954/209318236-79d3a5c3-2700-46c3-b59a-62d9c132a6c3.gif">\n</p>\n\n- Universal，Support multiple data export formats, including LabelU, COCO, Mask\n\n## Scenes\n\n### Computer Vision\n\n- Detection: Detection scenes for vehicles, license plates, pedestrians, faces, industrial parts, etc.\n- Classification: Detection of object classification, target characteristics, right and wrong judgments, and other classification scenarios\n- Semantic segmentation: Human body segmentation, panoramic segmentation, drivable area segmentation, vehicle segmentation, etc.\n- Text transcription: Text detection and recognition of license plates, invoices, insurance policies, signs, etc.\n- Contour detection: positioning line scenes such as human contour lines, lane lines, etc.\n- Key point detection: positioning scenes such as human face key points, vehicle key points, road edge key points, etc.\n\n## Usage\n\n-  [Guide](./docs/GUIDE.md) \n\n## Annotation Format\n\n-  [LabelU Annotation Format](./docs/annotation%20format/README.md)\n\n## Communication\n\nWelcome to the Opendatalab Wechat group！\n\n<p align="center">\n<img style="width: 400px" src="https://user-images.githubusercontent.com/25022954/208374419-2dffb701-321a-4091-944d-5d913de79a15.jpg">\n</p>\n\n\n\n## Links\n\n- [labelU-Kit](https://github.com/opendatalab/labelU-Kit)（Powered by labelU-Kit）\n\n## LICENSE\n\nThis project is released under the [Apache 2.0 license](./LICENSE).\n',
    'author': 'pengjinhu',
    'author_email': 'pengjinhu@pjlab.org.cn',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/opendatalab/labelU',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
