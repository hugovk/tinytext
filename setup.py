# encoding: utf-8
from __future__ import print_function, unicode_literals
from setuptools import setup


setup(
    name="tinytext",
    version="1.0.0",
    packages=["tinytext"],
    author="hugovk",
    description="A helpful text converter to change any normal text into "
                "cuter tinier text",
    url="https://github.com/hugovk/tinytext",
    long_description=open("README.md").read(),
    keywords=["botally", "tiny type", "tiny type", "tiny text", "cute text",
              "generator"],
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
        "Topic :: Text Processing",
    ],
    test_suite="tests",
)

# End of file
