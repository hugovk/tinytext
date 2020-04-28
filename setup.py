from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()


setup(
    name="tinytext",
    description="A helpful converter to change any normal text into cuter tinier text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="hugovk",
    url="https://github.com/hugovk/tinytext",
    license="MIT",
    keywords=[
        "botally",
        "tiny type",
        "tiny type",
        "tiny text",
        "cute text",
        "generator",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["tinytext = tinytext.cli:main"]},
    zip_safe=True,
    extras_require={"tests": ["hypothesis-auto", "pytest", "pytest-cov"]},
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Artistic Software",
        "Topic :: Text Processing",
    ],
)
