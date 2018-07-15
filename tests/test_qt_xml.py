import filecmp
import os

from vulture_whitelist.qt import QtWhitelistCreator
from tests import TESTS, SAMPLE_WHITELISTS


def test_whitelist_from_xml(tmpdir):
    whitelist = str(tmpdir.mkdir("whitelists").join("xml-whitelist.py"))
    c = QtWhitelistCreator(whitelist, 'sip')
    with open(whitelist, 'w') as outfile:
        xmldata = os.path.join(TESTS, 'test-data', 'xml-data')
        for xmldir in sorted(os.listdir(xmldata)):
            tmp = os.path.join(xmldata, xmldir)
            c._write_mod_whitelist(
                outfile, xmldir, c.name_set(tmp))
    expected_whitelist = os.path.join(SAMPLE_WHITELISTS, 'qtall.py')
    assert filecmp.cmp(whitelist, expected_whitelist, shallow=False)
