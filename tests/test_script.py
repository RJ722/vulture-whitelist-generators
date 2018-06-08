import filecmp
import os
import subprocess

from tests import TESTS, SAMPLE_WHITELISTS
from vulture_whitelist import __version__


def create_whitelist_from_test_sip_files():
    path = os.path.join(TESTS, 'test-data', 'sip')
    subprocess.call(['vulture-whitelist', 'sip'], cwd=path)


def test_qt_whitelist():
    create_whitelist_from_test_sip_files()
    whitelist_generated = os.path.join(
        TESTS, 'test-data', 'sip', 'whitelist.py')
    whitelist_sample = os.path.join(SAMPLE_WHITELISTS, 'qtbluetooth.py')
    assert filecmp.cmp(whitelist_generated, whitelist_sample, shallow=False)
    os.remove(whitelist_generated)


def test_version():
    version_string = 'vulture-whitelist {}\n'.format(__version__)
    assert subprocess.check_output(
        ['vulture-whitelist', '--version']).decode("utf_8") == version_string
