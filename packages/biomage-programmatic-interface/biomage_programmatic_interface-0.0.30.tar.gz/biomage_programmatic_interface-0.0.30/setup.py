from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

setup(
    name="biomage_programmatic_interface",
    version='0.0.30',
    author="Biomage Ltd",
    author_email="engineering@biomage.net",
    description="For programmatic upload of files to Cellencis",
    url = "https://github.com/biomage-org/programmatic_interface",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    keywords=['pypi', 'cicd', 'python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ]
)