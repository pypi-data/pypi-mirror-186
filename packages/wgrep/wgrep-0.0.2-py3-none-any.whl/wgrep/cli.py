from . import output
from .fileutils import save_to_file
from argparse import ArgumentParser

# TODO: try to use python click here
_parser = ArgumentParser(
    "wgrep",
    description="""Save whois information into a computer-readable file format (like toml, json, xml, etc.)"""
)

_parser.add_argument(
    'target',
    metavar='target',
    help="""The target to execute lookup."""
)

_parser.add_argument(
    'output',
    metavar="output",
    default='wgrep-output',
    help="""The file to save the output."""
)

_parser.add_argument(
    'format',
    metavar="format",
    help="""The format to save the data."""
)

args = _parser.parse_args()

_lnk = args.target
_out = args.output
_fmt = args.format.lower()

cvt_table = {
    "json": output.as_json,
    "xml": output.as_xml,
    "toml": output.as_toml
}

def main():
    try:
        data = cvt_table[_fmt](_lnk)
    except KeyError:
        print(f"error: {_fmt} was not implemented")
        exit(1)

    save_to_file(data, _out)


if __name__ == "__main__":
    main()
