from ..utils import replacer

IN, OUT = 'ŠČ', 'Щ'

convert = replacer({IN: OUT, IN.title(): OUT, IN.lower(): OUT.lower()})
