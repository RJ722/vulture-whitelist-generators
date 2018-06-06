import argparse

from . import qt


__version__ = '0.1'

CREATORS = {
    'sip': qt.QtWhitelistCreator
}


def get_creator(framework):
    return CREATORS.get(framework)


def _parse_args():
    version = "vulture-whitelist {0}".format(__version__)
    parser = argparse.ArgumentParser(prog='vulture-whitelist')
    parser.add_argument('--version', action='version', version=version)
    parser.add_argument('framework', choices=CREATORS.keys(), help=(
        'Framweork to generate a whitelist for.'))
    parser.add_argument('--name', nargs=1, default=['whitelist.py'], help=(
        'Name of the whitelist.'))
    parser.add_argument('--sip', nargs=1, default=['sip'], help=(
        'The sip binary to use when creating a whitelist for PyQt.'))
    return parser.parse_args()


def main():
    args = _parse_args()
    creator = get_creator(args.framework)
    creator(args).create()
