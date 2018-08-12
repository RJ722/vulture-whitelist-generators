import argparse

from vulture_whitelist import qt

__version__ = '0.1'

FRAMEWORKS = ('sip', )


def get_creator(framework, **kwargs):
    if framework == 'sip':
        return qt.QtWhitelistCreator(**kwargs)
    else:
        raise ValueError(
            "Invalid framework '{}', Supported frameworks are: '{}'.".format(
                framework, ', '.join(FRAMEWORKS)))


def _parse_args():
    version = "vulture-whitelist {}".format(__version__)
    parser = argparse.ArgumentParser(prog='vulture-whitelist')
    parser.add_argument('--version', action='version', version=version)
    parser.add_argument('framework', type=str, choices=FRAMEWORKS, help=(
        'Framweork to generate a whitelist for.'))
    parser.add_argument('--name', type=str, default='whitelist.py', help=(
        'Name of the whitelist.'))
    parser.add_argument('--sip', type=str, default='sip', help=(
        'The sip binary to use when creating a whitelist for PyQt.'))
    return parser.parse_args()


def main():
    args = _parse_args()
    creator = get_creator(args.framework, sip=args.sip)
    creator.create(args.name)
