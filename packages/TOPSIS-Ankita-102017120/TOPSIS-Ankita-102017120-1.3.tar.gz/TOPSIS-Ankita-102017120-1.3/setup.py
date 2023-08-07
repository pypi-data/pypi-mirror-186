import pathlib
from setuptools import setup,find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
with open('README.md', encoding="utf8") as file:
    README = file.read()

# This call to setup() does all the work
setup(
    name="TOPSIS-Ankita-102017120",
    version="1.3",
    description="This is a Python library for handling problems related to Multiple Criteria Decision Making(MCDM)",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Ankita Sharma",
    author_email="ankitasharma102002@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["TOPSIS-Ankita-102017120"],
    include_package_data=True,
    install_requires=['numpy','pandas'],
    entry_points={
        "console_scripts": [
            "topsis1=__main__:topsis",
        ]
    },
)