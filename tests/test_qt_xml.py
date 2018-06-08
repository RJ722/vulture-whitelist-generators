import filecmp
import os

from vulture_whitelist.qt import QtWhitelistCreator
from tests import TESTS, SAMPLE_WHITELISTS


def test_whitelist_from_xml():
    name = 'whitelist.py'
    c = QtWhitelistCreator(name, 'sip')
    with open(name, 'w') as outfile:
        xmldata = os.path.join(TESTS, 'test-data', 'xml-data')
        for xmldir in sorted(os.listdir(xmldata)):
            tmp = os.path.join(xmldata, xmldir)
            c._write_mod_whitelist(
                outfile, xmldir, c.name_set(tmp))
    expected_whitelist = os.path.join(SAMPLE_WHITELISTS, 'qtall.py')
    assert filecmp.cmp(name, expected_whitelist, shallow=False)
    os.remove(name)
