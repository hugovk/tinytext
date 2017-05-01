# encoding: utf-8
from __future__ import print_function, unicode_literals
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="tinytext",
    version="0.0.1",
    packages=['tinytext'],
    author="hugovk",
    description="A helpful text converter to change any normal text into "
                "cuter tinier text",
    url="https://github.com/hugovk/tinytext",
    long_description=open("README.md").read(),
    keywords="botally tiny type text cute generator",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Artistic Software",
    ],
)

# End of file
