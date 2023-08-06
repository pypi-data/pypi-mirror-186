# Always prefer setuptools over distutils
from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="hdss",
    version="1.1.0",
    description="HDSS - Hand-Drawn Shape Simulation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://boriskravtsov.com/",
    author="Boris Kravtsov",
    author_email="boriskravtsov.contacts@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Operating System :: MacOS :: MacOS X"
    ],
    packages=['hdss'],
    package_dir={'hdss': 'hdss'},
    include_package_data=False,
    install_requires=["opencv-python-headless", "numpy"]
)
