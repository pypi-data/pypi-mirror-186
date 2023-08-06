import setuptools
from datetime import datetime
now = datetime.now()
dt_string = now.strftime('%Y%m%d.%H%M')

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ed_design',
    version='0.1.7',
    author="Martin Vidkjaer",
    author_email="mav@envidan.dk",
    description="Python package developed by Envidan A/S scoping to follow the design of the company brand. This package is only for internal use.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://dev.azure.com/EnviDan-AS/ed_design",
    packages=setuptools.find_packages(),
    install_requires=[
        'matplotlib<3.6',
    ],
    python_requires='>=3.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
