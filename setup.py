# encoding: utf-8
from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="tinytext",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="1.0.0",
    packages=["tinytext"],
    author="hugovk",
    description="A helpful text converter to change any normal text into "
                "cuter tinier text",
    url="https://github.com/hugovk/tinytext",
    keywords=["botally", "tiny type", "tiny type", "tiny text", "cute text",
              "generator"],
    python_requires=">=3.4",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Artistic Software",
        "Topic :: Text Processing",
    ],
    test_suite="tests",
)

# End of file
