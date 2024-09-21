class Complex:
    def __init__(self, real, imaginary):
        self._real = real
        self._imaginary = imaginary

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, value):
        self._real = value

    @property
    def imaginary(self):
        return self._imaginary

    @imaginary.setter
    def imaginary(self, value):
        self._imaginary = value

    def __eq__(self, other):
        return self._real == other.real and self._imaginary == other.imaginary

    def __gt__(self, other):
        if self._real > other.real:
            return True
        if self._real < other.real:
            return False
        return self._real >= other.real

    def __repr__(self):
        return f"{self._real} + {self._imaginary}i"

    def __add__(self, other):
        return Complex(self._real + other.real, self._imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self._real - other.real, self._imaginary - other.imaginary)

