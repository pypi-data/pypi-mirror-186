from setuptools import setup, find_packages
import os
import re

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


def get_version():
    init = open(os.path.join(ROOT, 'skorch_forecasting', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


name = 'skorch_forecasting'
author = 'ramonamez'
description = 'Sklearn interface to state-of-the-art forecasting with ' \
              'neural networks.'

setup(
    name=name,
    version=get_version(),
    author=author,
    packages=find_packages(),
    description=description,
    python_requires='>=3.7',
    install_requires=[
        'numpy>=1.22.0',
        'pandas>=1.4.0',
        'scikit-learn>=1.0.0',
        'skorch>=0.10.0',
        'torch>=1.5.0',
        'pytorch-forecasting>=0.9.0'
    ]
)
