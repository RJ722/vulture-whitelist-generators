import filecmp
import os
import subprocess

from tests import TESTS, SAMPLE_WHITELISTS
from vulture_whitelist import __version__


def create_whitelist_from_test_sip_files(name):
    path = os.path.join(TESTS, 'test-data', 'sip')
    subprocess.call(['vulture-whitelist', 'sip', '--name', name], cwd=path)


def test_qt_whitelist(tmpdir):
    whitelist = str(tmpdir.mkdir("whitelists").join("whitelist.py"))
    create_whitelist_from_test_sip_files(whitelist)
    whitelist_sample = os.path.join(SAMPLE_WHITELISTS, 'qtbluetooth.py')
    assert filecmp.cmp(whitelist, whitelist_sample, shallow=False)


def test_version():
    version_string = 'vulture-whitelist {}\n'.format(__version__)
    assert subprocess.check_output(
        ['vulture-whitelist', '--version']).decode("utf_8") == version_string
