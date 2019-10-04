from __future__ import division
from math import gcd


class Rational(object):
    def __init__(self, numer, denom):
        gcd_ = gcd(numer, denom)
        if (numer < 0 < denom) or (denom < 0 < numer):
            self.numer = -(abs(numer//gcd_))
        else:
            self.numer = abs(numer//gcd_)
        self.denom = abs(denom//gcd_)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational((self.numer * other.denom)+(self.denom * other.numer), self.denom * other.denom)


    def __sub__(self, other):
        return Rational((self.numer * other.denom)-(self.denom * other.numer), self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power < 0:
            return Rational(self.denom ** abs(power), self.numer ** abs(power))
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        return (base ** self.numer) ** (1/self.denom)
