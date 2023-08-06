from ..utils import translator

IN, OUT = "AEYIOU", "АЕИІОУ"

convert = translator(IN + IN.lower(), OUT + OUT.lower())
