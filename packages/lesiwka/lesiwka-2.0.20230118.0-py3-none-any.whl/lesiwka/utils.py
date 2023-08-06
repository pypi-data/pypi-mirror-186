import re


class Converter(object):
    def __init__(self, split, valid, action):
        self.pattern = re.compile(split, re.UNICODE)
        self.word_cls = get_word_cls(valid, action)

    def __call__(self, text):
        words = []

        word = None
        for string in self.pattern.split(text):
            word = self.word_cls(string, prev=word)
            words.append(word)

        return "".join(word.convert() for word in words)


def applier(*funcs):
    def _(word):
        for func in funcs:
            word = func(word)
        return word

    return _


def get_word_cls(valid, action):
    valid = set(valid)

    class Word(object):
        def __init__(self, word='', prev=None, next_=None):
            self.word = word
            self._prev = prev
            self._next = next_
            self.abbr = False
            if prev is not None:
                prev.set_next(self)

        def __repr__(self):
            return repr(self.word)

        def convert(self):
            if not self:
                return self.word

            orig = self.word
            p, n = self.get_prev(), self.get_next()
            action(self)

            if orig.isupper() and (p and p.is_upper() or n and n.is_upper()):
                return self.word.upper()

            if self.word and orig.istitle():
                return self.word[0].upper() + self.word[1:].lower()

            return self.word

        def __bool__(self):
            return not set(self.word.upper()) - valid

        def has_stop(self):
            if self._next is not None:
                return self._next.word.startswith(".")

        def continues(self):
            if self._next is not None:
                return (
                    self._next.word in "-\u2010"
                    or self._next.word.strip() in '"„“”«'
                )

        def get_next(self):
            if self._next is not None:
                return self._next if self._next else self._next.get_next()

        def get_prev(self):
            if self._prev is not None:
                return self._prev if self._prev else self._prev.get_prev()

        def is_upper(self):
            return self.word.isupper()

        def set_next(self, next_):
            self._next = next_

        def __add__(self, other):
            self.word += other
            return self

        def __radd__(self, other):
            self.word = other + self.word
            return self

        def apply(self, func, index=0):
            self.word = self.word[:index] + func(self.word[index:])
            return self

        def replace(self, old, new, count=-1):
            self.word = self.word.replace(old, new, count)
            return self

        def re_replace(self, pattern, new):
            self.word = new.join(t for t in pattern.split(self.word))
            return self

        def startswith(self, prefix):
            return self.word.startswith(prefix)

        def strip(self, chars):
            self.word = self.word.strip(chars)
            return self

        def lstrip(self, chars):
            self.word = self.word.lstrip(chars)
            return self

        def translate(self, table):
            self.word = self.word.translate(table)
            return self

        def upper(self):
            self.word = self.word.upper()
            return self

    return Word


def replacer(table, count=-1):
    def _(word):
        for i, o in table.items():
            word = word.replace(i, o, count)
        return word

    return _


def translator(*args):
    trans = str.maketrans(*args)

    def _(word):
        return word.translate(trans)

    return _
