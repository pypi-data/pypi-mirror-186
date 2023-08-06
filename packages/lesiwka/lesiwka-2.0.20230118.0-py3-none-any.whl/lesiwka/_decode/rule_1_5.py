from ..utils import translator

IN, OUT = 'J', 'Й'

convert = translator(IN + IN.lower(), OUT + OUT.lower())
