import math


class Pythagoras(object):

    def __init__(self, a=None, b=None, c=None):
        self._a = a
        self._b = b
        self._c = c

        count = 0
        if self._a is None:
            count += 1
        if self._b is None:
            count += 1
        if self._c is None:
            count += 1

        if count > 1:
            raise Exception("More than one of the values are None.")

    @property
    def a(self):
        if self._a is None:
            return math.sqrt(self.c**2 - self.b**2)
        else:
            return self._a

    @property
    def b(self):
        if self._b is None:
            return math.sqrt(self.c**2 - self.a**2)
        else:
            return self._b

    @property
    def c(self):
        if self._c is None:
            return math.sqrt(self.a**2 + self.b**2)
        else:
            return self._c


o = Pythagoras(a=3, b=4)
print(o.c)