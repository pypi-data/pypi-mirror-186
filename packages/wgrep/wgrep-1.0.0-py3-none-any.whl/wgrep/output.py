import whois

import json
import toml
from dict2xml import dict2xml


def _unpack(website):
    data = whois.whois(website)
    return json.loads(str(data))


def as_json(website) -> dict:
    """Will return a JSON (dict) containing
    the whois lookup of `website`."""

    return _unpack(website)


def as_xml(website) -> str:
    """Will return a string representing a xml
    document containing the whois lookup of `website`."""

    return dict2xml(_unpack(website))


def as_toml(website):
    """Will return a string representing a TOML
    document containing the whois lookup of `website`."""

    return toml.dumps(_unpack(website))
