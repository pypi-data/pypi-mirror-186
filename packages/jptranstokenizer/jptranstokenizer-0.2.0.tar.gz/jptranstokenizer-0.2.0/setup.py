# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['jptranstokenizer', 'jptranstokenizer.mainword', 'jptranstokenizer.subword']

package_data = \
{'': ['*']}

install_requires = \
['SudachiTra>=0.1.7,<0.2.0',
 'pyknp>=0.6.1,<0.7.0',
 'sentencepiece>=0.1.96,<0.2.0',
 'spacy>=3.2.0,<4.0.0',
 'transformers>=4.7.0,<5.0.0']

setup_kwargs = {
    'name': 'jptranstokenizer',
    'version': '0.2.0',
    'description': 'Japanese tokenizer with transformers library',
    'long_description': '<div id="top"></div>\n\n<h1 align="center">jptranstokenizer: Japanese Tokenzier for transformers</h1>\n\n<p align="center">\n  <img alt="Python" src="https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue">\n  <a href="https://pypi.python.org/pypi/jptranstokenizer">\n    <img alt="pypi" src="https://img.shields.io/pypi/v/jptranstokenizer.svg">\n  </a>\n  <a href="https://github.com/retarfi/jptranstokenizer#licenses">\n    <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">\n  </a>\n  <a href="https://github.com/retarfi/jptranstokenizer/actions/workflows/test.yml">\n    <img alt="Test" src="https://github.com/retarfi/jptranstokenizer/actions/workflows/test.yml/badge.svg">\n  </a>\n  <a href="https://github.com/retarfi/jptranstokenizer/releases">\n    <img alt="GitHub release" src="https://img.shields.io/github/v/release/retarfi/jptranstokenizer.svg">\n  </a>\n</p>\n\nThis is a repository for japanese tokenizer with HuggingFace library.  \nYou can use `JapaneseTransformerTokenizer` like `transformers.BertJapaneseTokenizer`.  \n**issue は日本語でも大丈夫です。**\n\n## Documentations\n\nDocumentations are available on [readthedoc](https://jptranstokenizer.readthedocs.io/en/latest/index.html).\n## Install\n```\npip install jptranstokenizer\n```\n\n## Quickstart\n\nThis is the example to use `jptranstokenizer.JapaneseTransformerTokenizer` with [sentencepiece model of nlp-waseda/roberta-base-japanese](https://huggingface.co/nlp-waseda/roberta-base-japanese) and Juman++.  \nBefore the following steps, you need to **install pyknp and Juman++**.\n\n```python\n>>> from jptranstokenizer import JapaneseTransformerTokenizer\n>>> tokenizer = JapaneseTransformerTokenizer.from_pretrained("nlp-waseda/roberta-base-japanese")\n>>> tokens = tokenizer.tokenize("外国人参政権")\n# tokens: [\'▁外国\', \'▁人\', \'▁参政\', \'▁権\']\n```\n\nNote that different dependencies are required depending on the type of tokenizer you use.  \nSee also [Quickstart on Read the Docs](https://jptranstokenizer.readthedocs.io/en/latest/quickstart.html)\n\n\n## Citation\n\n\n**There will be another paper.\nBe sure to check here again when you cite.**\n\n### This Implementation\n\n```\n@misc{suzuki-2022-github,\n  author = {Masahiro Suzuki},\n  title = {jptranstokenizer: Japanese Tokenzier for transformers},\n  year = {2022},\n  publisher = {GitHub},\n  journal = {GitHub repository},\n  howpublished = {\\url{https://github.com/retarfi/jptranstokenizer}}}\n```\n\n\n## Related Work\n- Pretrained Japanese BERT models (containing Japanese tokenizer)\n  - Autor NLP Lab. in Tohoku University\n  - https://github.com/cl-tohoku/bert-japanese\n- SudachiTra\n  - Author Works Applications\n  - https://github.com/WorksApplications/SudachiTra\n- UD_Japanese-GSD\n  - Author megagonlabs\n  - https://github.com/megagonlabs/UD_Japanese-GSD\n- Juman++\n  - Author Kurohashi Lab. in Universyti of Kyoto\n  - https://github.com/ku-nlp/jumanpp\n',
    'author': 'Masahiro Suzuki',
    'author_email': 'msuzuki9609@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
