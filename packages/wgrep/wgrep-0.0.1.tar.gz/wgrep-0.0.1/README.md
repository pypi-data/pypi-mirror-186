# Whois Grep

Gather whois information of a website into a file format that
can be parsed into pretty much any programming language.

## Usage

```python
import wgrep

data = wgrep.as_json('www.somewebsite.com') # data = dict
```

## Currently supported output formats

- json
- csv
- toml

