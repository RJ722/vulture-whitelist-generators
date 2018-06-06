from vulture_whitelist import main, qt


def test_framework():
    assert main.get_creator('sip') == qt.QtWhitelistCreator
