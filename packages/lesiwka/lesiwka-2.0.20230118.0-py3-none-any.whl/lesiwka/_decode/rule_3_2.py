from ..utils import translator

TRANSLATE = {
    'Đ': 'ДЖ',
    'Ƶ': 'ДЗ',
}


def get_convert():
    data = TRANSLATE.copy()
    data.update({i.lower(): o.lower() for i, o in TRANSLATE.items()})
    return translator(data)


convert = get_convert()
