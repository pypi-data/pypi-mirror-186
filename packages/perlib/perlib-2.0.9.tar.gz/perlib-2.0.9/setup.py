import setuptools
from setuptools import setup, find_packages
from perlib.__init__ import __version__

with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

NAME = 'perlib'
VERSION = __version__
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'
URL = 'https://github.com/Ruzzg/perlib'
AUTHOR = 'Rüzgar Ersin Kanar'
DESCRIPTION = "Deep learning, Machine learning and Statistical learning for humans."
AUTHOR_EMAIL = 'ruzgarknr@gmail.com'
LICENSE = 'Apache Software License'
KEYWORDS = 'perlib,tensorflow,machine learning,deep learning'

setup(
    name=NAME,
    version=VERSION,
    description = DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    packages = find_packages(),
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    install_requires =[ "catboost==1.1.1",
                        "Flask==2.2.2",
                        "joblib==1.1.1",
                        "keras==2.10.0",
                        "keras_tcn==3.5.0",
                        "lightgbm==3.2.1",
                        "loguru==0.6.0",
                        "matplotlib==3.6.2",
                        "numpy==1.23.5",
                        "pandas==1.5.2",
                        "python_dateutil==2.8.2",
                        "scikit_learn==1.2.0",
                        "scipy==1.9.3",
                        "statsmodels==0.13.2",
                        "tensorflow==2.10.0",
                        "tqdm==4.64.1",
                        "xgboost==1.5.0"],
    keywords=KEYWORDS,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)