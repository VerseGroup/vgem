import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

VERSION = "1.1.0"
DESCRIPTION="VerseGroups encryption manager class (RSA and Fernet wrapped AES sessions through RSA) for secure transmission of data"
KEYWORDS=['RSA', 'FERNET', 'vgem', 'Encryption Manager', 'Encryption', 'Verse Group']

setup(
    name="vgem",
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/VerseGroup/vgem-python",
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
    packages=find_packages(exclude=("tests",)),
    keywords=KEYWORDS
)