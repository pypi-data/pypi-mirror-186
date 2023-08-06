from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'Parse whois data into program-readable formats (like JSON, XML, TOML, etc.)'
LONG_DESCRIPTION = """A package that allows you to convert whois data to computer-readable data formats (like JSON, XML, etc.)
It is convenient to make lookup programs or API integrations."""

setup(
    name="wgrep",
    version=VERSION,
    author="callope",
    author_email="callope@proton.me",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['python-whois', 'toml', 'dict2xml'],
    keywords=['python', 'whois', 'lookup', 'api integration', 'information'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
