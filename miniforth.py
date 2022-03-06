# Copyright (c) 2022 fts

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#!/usr/bin/env python3
# A minimal FORTH, no builtin words beyond `:`


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
