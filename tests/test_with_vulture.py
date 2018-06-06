from . import SAMPLE_WHITELISTS

import os
import vulture

v = vulture.Vulture(verbose=True)
#  Feed the pre-generated whitelist to Vulture.
v.scavenge([os.path.join(SAMPLE_WHITELISTS, 'qtall.py')])


def check(items_or_names, expected_names):
    if isinstance(items_or_names, set):
        # items_or_names is a set of strings.
        assert items_or_names == set(expected_names)
    else:
        # items_or_names is a list of vulture.Item objects.
        names = sorted(item.name for item in items_or_names)
        expected_names = sorted(expected_names)
        assert names == expected_names


def test_closeEvent_method():
    code = """\
from PyQt5.QtWidgets import QWidget

class Example(QWidget):
    def closeEvent(self, event):
        pass
"""
    v.scan(code)
    check(v.defined_classes, ['Example'])
    check(v.unused_classes, ['Example'])
    check(v.defined_funcs, ['closeEvent'])
    check(v.unused_funcs, [])
