import pytest

from vulture_whitelist import main, qt


def test_get_creator_qt():
    assert type(main.get_creator(
        'sip', sip='/path/to/sip')) == qt.QtWhitelistCreator


def test_get_creator_invalid_framework():
    with pytest.raises(ValueError) as err:
        main.get_creator('sipp', sip='/path/to/sip')
    assert err.match(
        "Invalid framework 'sipp', Supported frameworks are: 'sip'")
