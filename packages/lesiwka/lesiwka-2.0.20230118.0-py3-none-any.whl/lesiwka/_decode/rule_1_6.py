from ..utils import replacer

IN, OUT = 'JI', 'Ї'

convert = replacer({IN: OUT, IN.title(): OUT, IN.lower(): OUT.lower()})
