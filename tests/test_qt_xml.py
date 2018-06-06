from . import TESTS, SAMPLE_WHITELISTS

import filecmp
import os

from vulture_whitelist.qt import QtWhitelistCreator


class MockArg:

    def __init__(self):
        self.sip = 'sip'
        self.name = 'xml-whitelist.py'


def test_whitelist_from_xml():
    args = MockArg()
    c = QtWhitelistCreator(args)
    with open(args.name, 'w') as outfile:
        xmldata = os.path.join(TESTS, 'test-data', 'xml-data')
        for xmldir in sorted(os.listdir(xmldata)):
            tmp = os.path.join(xmldata, xmldir)
            c._write_mod_whitelist(
                outfile, xmldir, c.name_set(tmp))
    expected_whitelist = os.path.join(SAMPLE_WHITELISTS, 'qtall.py')
    assert filecmp.cmp(args.name, expected_whitelist, shallow=False)
    os.remove(args.name)
