# Whois Grep

Gather whois information of a website into a file format that
can be parsed into pretty much any programming language.

## Installation

Simply install this package using `pip`:

```
$ pip install wgrep
```

## Usage

This package is pretty easy to use, simply `import wgrep` and call the converter function
(it has the format `as_{choosen format}`) passing the link of the website to get the whois
information as an argument. Like this:

```python
import wgrep

data_json = wgrep.as_json('www.somewebsite.com')
data_xml = wgrep.as_xml('www.somewebsite.com')
data_toml = wgrep.as_toml('www.somewebsite.com')
```

## Currently supported output formats

- json
- csv
- toml

