# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cfutils']

package_data = \
{'': ['*']}

install_requires = \
['Click>=8.0.0,<9.0.0',
 'biopython>=1.78,<2.0',
 'matplotlib>=3.0.0,<4.0.0',
 'ssw>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['cfutils = cfutils.cli:cli']}

setup_kwargs = {
    'name': 'cfutils',
    'version': '0.0.0.dev58',
    'description': 'Chromatogram File Utils',
    'long_description': '[![Readthedocs](https://readthedocs.org/projects/cfutils/badge/?version=latest)](https://cfutils.readthedocs.io/en/latest/?badge=latest)\n[![Build Status](https://img.shields.io/travis/y9c/cfutils.svg)](https://travis-ci.org/y9c/cfutils)\n[![Pypi Releases](https://img.shields.io/pypi/v/cfutils.svg)](https://pypi.python.org/pypi/cfutils)\n[![Downloads](https://pepy.tech/badge/cfutils)](https://pepy.tech/project/cfutils)\n\n**Chromatogram File Utils**\n\nFor Sanger sequencing data visualizing, alignment, mutation calling, and trimming etc.\n\n## Demo\n\n![plot chromatogram with mutation](https://raw.githubusercontent.com/y9c/cfutils/master/data/plot.png)\n\n> command to generate the demo above\n\n```bash\ncfutils mut --query ./data/B5-M13R_B07.ab1 --subject ./data/ref.fa --outdir ./data/ --plot\n```\n\n## How to use?\n\n- You can have mutation detection and visualization in one step using the command line.\n\n```bash\ncfutils mut --help\n```\n\n- You can also integrate the result matplotlib figures and use it as a python module.\n\nAn example:\n\n```python\nimport matplotlib.pyplot as plt\nimport numpy as np\n\nfrom cfutils.parser import parse_abi\nfrom cfutils.show import plot_chromatograph\n\nseq = parse_abi("./data/B5-M13R_B07.ab1")\npeaks = seq.annotations["peak positions"][100:131]\n\nfig, axes = plt.subplots(2, 1, figsize=(12, 6), sharex=True)\nplot_chromatograph(\n    seq,\n    region=(100, 130),\n    ax=axes[0],\n    show_bases=True,\n    show_positions=True,\n    color_map=dict(zip("ATGC", ["C0", "C2", "C1", "C4"])),\n)\naxes[1].bar(peaks, np.random.randn(len(peaks)), color="0.66")\nplt.show()\n```\n\n![plot chromatogram in_matplotlib](https://raw.githubusercontent.com/y9c/cfutils/master/data/matplotlib_example.png)\n\n## How to install?\n\n### form pypi\n\n_(use this way ONLY, if you don\'t know what\'s going on)_\n\n```bash\npip install --user cfutils\n```\n\n### manipulate the source code\n\n- clone from github\n\n```bash\ngit clone git@github.com:y9c/cfutils.git\n```\n\n- install the dependence\n\n```bash\nmake init\n```\n\n- do unittest\n\n```bash\nmake test\n```\n\n## ChangeLog\n\n- Reverse completement the chromatogram file. (Inspired by Snapgene)\n- build as python package for pypi\n- fix bug that highlighting wrong base\n- replace blastn with buildin python aligner\n\n## TODO\n\n- [ ] call mutation by alignment and plot Chromatogram graphic\n- [ ] add a doc\n- [x] change xaxis by peak location\n- [ ] fix bug that chromatogram switch pos after trim\n- [x] wrap as a cli app\n- [ ] return quality score in output\n- [ ] fix issue that selected base is not in the middle\n- [ ] fix plot_chromatograph rendering bug\n\n- [ ] add projection feature to make align and assemble possible\n',
    'author': 'Ye Chang',
    'author_email': 'yech1990@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/yech1990/cfutils',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
