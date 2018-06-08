import argparse

from vulture_whitelist import __version__, qt

CREATORS_META = {
    'sip': (qt.QtWhitelistCreator, 'sip')
}


def get_creator(framework):
    return CREATORS_META.get(framework)


def _parse_args():
    version = "vulture-whitelist {}".format(__version__)
    parser = argparse.ArgumentParser(prog='vulture-whitelist')
    parser.add_argument('--version', action='version', version=version)
    parser.add_argument('framework', choices=CREATORS_META.keys(), help=(
        'Framweork to generate a whitelist for.'))
    parser.add_argument('--name', nargs=1, default=['whitelist.py'], help=(
        'Name of the whitelist.'))
    parser.add_argument('--sip', nargs=1, default=['sip'], help=(
        'The sip binary to use when creating a whitelist for PyQt.'))
    return parser.parse_args()


def main():
    args = _parse_args()
    creator, argv = get_creator(args.framework)
    creator(args.name[0], argv).create()
