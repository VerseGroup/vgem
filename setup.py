import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

VERSION = "1.0.2"
DESCRIPTION="VerseGroups encryption manager class (RSA and AES sessions through RSA) for secure transmission of data"

setup(
    name="vgem",
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
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
    ],
    include_package_data=True,
    python_requires='>=3.6',    
    install_requires=["cryptography", "pycparser", "cffi"],
    package_dir={'':'src'},
)