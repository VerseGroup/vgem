import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

VERSION = "1.0.0"
DESCRIPTION=""

setup(
    name="vg-em",
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/VerseGroup/EM-python",
    author="VERSEGROUPLLC",
    author_email="officialversegroupllc@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9"
    ],
    packages=["src"],
    include_package_data=True,
    install_requires=["cryptography", "pycparser", "cffi"],
    packages=find_packages(exclude=("tests",)),
)