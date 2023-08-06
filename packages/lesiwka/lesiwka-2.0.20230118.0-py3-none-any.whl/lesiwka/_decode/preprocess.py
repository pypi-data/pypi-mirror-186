from ..diacritics import ACUTE, CARON
from ..utils import replacer

COMBININGS = {
    'C' + CARON: 'Č',
    'S' + CARON: 'Š',
    'Z' + CARON: 'Ž',
    'Ć': 'C' + ACUTE,
    'Ĺ': 'L' + ACUTE,
    'Ń': 'N' + ACUTE,
    'Ŕ': 'R' + ACUTE,
    'Ś': 'S' + ACUTE,
    'Ź': 'Z' + ACUTE,
    'Ǵ': 'G' + ACUTE,
    'Ḱ': 'K' + ACUTE,
    'Ḿ': 'M' + ACUTE,
    'Ṕ': 'P' + ACUTE,
}


def get_convert():
    data = COMBININGS.copy()

    for i, o in COMBININGS.items():
        data[i.lower()] = o.lower()

    return replacer(data)


convert = get_convert()
