from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["lxml"]

setup(
    name="parse-schema",
    version="0.0.1",
    author="zavx0z",
    author_email="zavx0z@yahoo.com",
    description="A package to create structure web-elements schema",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/zavx0z/parse-schema",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
