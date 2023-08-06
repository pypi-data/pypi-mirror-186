import codecs
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name="ytcli",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "click",
        "pytube"
    ],
    entry_points="""
    [console_scripts]
    ytcli=ytcli:ytcli
    """,
    description="ytcli is command line interface for YouTube",
    long_description_content_type="text/markdown",
    long_description=long_description,
)
