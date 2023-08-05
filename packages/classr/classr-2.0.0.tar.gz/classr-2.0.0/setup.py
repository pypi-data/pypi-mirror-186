# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['classr']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'classr',
    'version': '2.0.0',
    'description': 'Use microclassifiers in the cloud for spam detection, sentiment analysis and more.',
    'long_description': "# Classr SDK for Python\nUse microclassifiers in the cloud for spam detection, sentiment analysis and more.\n\n![Classr logo](./logo.svg)\n\n## Requirements\n\n- Python 3.6 or newer\n\n## Installation\n\nThe Classr SDK for Python can be installed using `pip`:\n\n```sh\npip install classr\n```\n\n## Usage\n\nInitiaize your microclassifier by passing its UUID to the `Classr` constructor like so:\n\n```python\nfrom classr import Classr\n\n# Initialize cloud microclassifier.\nclassifier = Classr('acd78708-850b-4cea-aeaa-23cec50d13b6')\n```\n\nNow, call the `classify` or `get_info` functions of `classifier` to make use of it:\n\n```python\n# Classify unseen input.\ndocument = input('Enter your input: ')\nprint(f'Predicted class: {classifier.classify(document)}')\n\n# Print macro F1 score of classifier.\ninfo = classifier.get_info()\nprint(f'Classifier macro F1 score is: {info.f1_score}')\n```\n\nIf you'd like to use a self-hosted deployment of the Classr application (i.e. not the default official API), you can\npass a different base URL when constructing your `Classr` object:\n\n```python\nfrom classr import Classr\n\n# Initialize cloud microclassifier.\nclassifier = Classr('acd78708-850b-4cea-aeaa-23cec50d13b6', 'https://self-hosted-classr.example.com/')\n```\n\n## Related Projects\n\nThis SDK is for the official [Classr application](https://github.com/lambdacasserole/classr) (but will work with a\nself-hosted deployment too, of course).\n\n## License\n\n[MIT](LICENSE) © [lambdacasserole](https://github.com/lambdacasserole).\n",
    'author': 'Saul Johnson',
    'author_email': 'saul.a.johnson@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lambdacasserole/classr-py.git',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
