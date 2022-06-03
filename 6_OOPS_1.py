class ComplexNumbers():
    def __init__(self, real = 0, imaginary = 0):
        self._real = real
        self._imaginary = imaginary
    
    def __add__(self, other):
        self._real += other._real
        self._imaginary += other._imaginary
        return self
    
    def __mul__(self, other):
        re = (self._real * other._real) - (self._imaginary * other._imaginary)
        im = (self._real * other._imaginary) + (self._imaginary * other._real)
        self._real = re
        self._imaginary = im
        return self

    def __str__(self):
        return str(self._real) + ' + i' + str(self._imaginary)

C1 = ComplexNumbers(3, 4)
C2 = ComplexNumbers(6, 8)

print('C1  =', C1)
print('C2  =', C2)
C1 = C1 + C2
print('add =', C1)
C1 = C1 * C2
print('mul =', C1)

C3 = ComplexNumbers()
print(C3)