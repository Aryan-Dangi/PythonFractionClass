from math import gcd
class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()

    def _simplify(self):
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __add__(self, other):
        if isinstance(other, Fraction):
            num = self.numerator * other.denominator + other.numerator * self.denominator
            den = self.denominator * other.denominator
        else:
            num = self.numerator + other * self.denominator
            den = self.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            num = self.numerator * other.denominator - other.numerator * self.denominator
            den = self.denominator * other.denominator
        else:
            num = self.numerator - other * self.denominator
            den = self.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            num = self.numerator * other.numerator
            den = self.denominator * other.denominator
        else:
            num = self.numerator * other
            den = self.denominator
        return Fraction(num, den)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            num = self.numerator * other.denominator
            den = self.denominator * other.numerator
        else:
            num = self.numerator
            den = self.denominator * other
        return Fraction(num, den)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}" if self.denominator != 1 else f"{self.numerator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def to_float(self):
        return self.numerator / self.denominator
