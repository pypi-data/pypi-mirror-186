from ..utils import translator

IN, OUT = 'ŽČŠ', 'ЖЧШ'

convert = translator(IN + IN.lower(), OUT + OUT.lower())
