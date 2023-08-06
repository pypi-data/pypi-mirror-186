import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Topsis-Aditi-102003512",
    version="1.0.1",
    description="Calculate TOPSIS Ranks",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Aditi Singh",
    author_email="asingh7_be20@thapar.edu",
    url="https://github.com/aditisingh-20/Topsis-Aditi-102003512/tree/v_01",
    download_url="https://github.com/aditisingh-20/Topsis-Aditi-102003512/archive/refs/tags/v_01.tar.gz",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["TOPSIS"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "TOPSIS=TOPSIS.__main__:main",
        ]
    },
)