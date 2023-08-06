from collections import OrderedDict

from .diacritics import ACUTE
from .utils import replacer, translator

TRANSLATE = OrderedDict(
    (
        (ACUTE, "'"),
        ("Ƶ", "QQ"),
        ("Č", "CQ"),
        ("Š", "SQ"),
        ("Ž", "ZQ"),
        ("Đ", "DQ"),
    )
)


def get_asciilator():
    data = TRANSLATE.copy()
    data.update((i.lower(), o.lower()) for i, o in TRANSLATE.items())

    return translator(dict(data))


def get_deasciilator():
    replace = OrderedDict((v, k) for k, v in TRANSLATE.items())

    data = replace.copy()
    data.update((i.title(), o) for i, o in replace.items())
    data.update((i.lower(), o.lower()) for i, o in replace.items())

    return replacer(data)


asciilator = get_asciilator()
deasciilator = get_deasciilator()

del get_asciilator
del get_deasciilator
