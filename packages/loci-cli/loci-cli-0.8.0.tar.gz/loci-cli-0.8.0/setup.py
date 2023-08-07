import setuptools
from loci import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="loci-cli",
    author="TheTwitchy",
    version=__version__,
    author_email="thetwitchy@thetwitchy.com",
    description="The official Loci CLI tool. Performs basic Loci Notes tasks from any command line.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/loci-notes/loci-cli",
    packages=setuptools.find_packages(),
    install_requires=[
        "click",
        "requests",
        "rich",
        "pendulum"
    ],
    entry_points={
        "console_scripts": [
            "loci = loci.main:loci_cli",
        ],
    },
)
