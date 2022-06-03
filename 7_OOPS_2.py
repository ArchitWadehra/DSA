class Poly():
    def __init__(self, coef = []):
        self._coef = coef
    
    def copy(self, other):
        self._coef = other._coef

    def set_coef(self, deg, coef):
        if len(self._coef) > deg:
            self._coef[len(self._coef) - deg - 1] = coef
        else:
            self._coef = [coef] + [0]*(deg-len(self._coef)) + self._coef
        return self

    def add_coef(self, deg, coef):
        if len(self._coef) > deg:
            self._coef[len(self._coef) - deg - 1] += coef
        else:
            self._coef = [coef] + [0]*(deg-len(self._coef)) + self._coef
        return self        

    def __str__(self):
        ans = ''
        for i in range(len(self._coef)):
            if self._coef[i] != 0:
                if len(self._coef) - i - 1 == 0:
                    ans = ans + str(self._coef[i])
                else:
                    ans = ans + str(self._coef[i]) + 'x^' + str(len(self._coef) - i - 1) + ' + '
        return ans

    def __add__(self, other):      
        new = Poly()
        for deg in range(len(self._coef)):
            new.add_coef(deg, self._coef[len(self._coef) - deg - 1])
        for deg in range(len(other._coef)):
            new.add_coef(deg, other._coef[len(other._coef) - deg - 1])
        return new

    def __sub__(self, other):
        new = Poly()
        for deg in range(len(self._coef)):
            new.add_coef(deg, self._coef[len(self._coef) - deg - 1])
        for deg in range(len(other._coef)):
            new.add_coef(deg, -1 * other._coef[len(other._coef) - deg - 1])
        return new        

    def __mul__(self, other):
        new = Poly()
        for i in range(len(self._coef)):
            for j in range(len(other._coef)):
                new.add_coef(i + j, self._coef[len(self._coef) - i - 1] * other._coef[len(other._coef) - j - 1])
        return new

    def __eq__(self, other):
        if len(self._coef) == len(other._coef):
            for i in range(len(self._coef)):
                if self._coef[i] != other._coef[i]:
                    return False
            return True
        else:
            return False

# Tests
P1 = Poly([1,2,3])
print(P1)
P1.set_coef(1, 99)
P1.set_coef(10, 69)
print(P1)

P1.add_coef(1,1)
print(P1)

P2 = Poly([5,5,5,0,0])
P3 = P1 + P2
print(P3)
P3 = P3 - P2
print(P3)

P4 = Poly([1,2]) * Poly([3,4])
print(P4)

print(P1 == P2)
print(Poly([1,2]) == Poly([1,2]))