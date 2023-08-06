from ..utils import translator

IN, OUT = 'BVHGDZKLMNPRSTFXC', 'БВГҐДЗКЛМНПРСТФХЦ'

convert = translator(IN + IN.lower(), OUT + OUT.lower())
