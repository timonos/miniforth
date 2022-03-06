# A minimal FORTH, no builtin words beyond `:`

#!/usr/bin/env python3

class FORTH (object):
    def __init__(self, src: str):
        self.src = src
        self.dct = {}
        self.stk = []

        self.defn = ':'
        self.term = ';'

    def define(self):
        """ Define a single word on the toplevel """
        if len(self.src) != 0 and self.src[0] == self.defn:
            index = self.src.index(self.term)
            word  = self.src[1:index]

            self.dct[word[0]] = word[1:]
            self.src = self.src[index + 1:]

            return True

    def eval(self, word: str = []):
        """ Evaluate an expression """
        if len(word) == 0 and len(self.src) != 0:
            return self.eval(self.src)

        for w in word:
            if w.isnumeric(): self.stk.append(float(w))
            elif w is self.term: return self.stk[-1]
            else: self.eval(self.dct[w])

    def load(self):
        """ Load word definitions """
        self.src = self.src.replace(self.term, f' {self.term} ')
        self.src = self.src.replace(self.defn, f' {self.defn} ')
        self.src = self.src.split()

        while self.define(): continue

forth = FORTH(': a 3 4; a;')
forth.load()
print(forth.eval())