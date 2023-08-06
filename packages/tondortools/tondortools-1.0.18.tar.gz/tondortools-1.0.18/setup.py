import pathlib
from setuptools import setup, find_packages

from tondortools import __version__

HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work'
setup(
    name="tondortools",
    version=__version__,
    description="Package inludes tools for Tondor",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/gisat/tondor_tools",
    author="Michal Opetal, Sivasankar Arul",
    author_email="michal.opletal@gisat.cz, sivasankar.arul@gisat.cz",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9"],
    packages=["tondortools", 'tondortools.tiles_gpkg'],
    package_data = {'tiles_gpkg': ['*.gpkg']},
    include_package_data=True
    )
