from ..diacritics import ACUTE
from ..utils import translator

IN, OUT = ACUTE, 'Ь'

convert = translator(IN, OUT.lower())
