# Inheritance

class C2dVector:
    def __init__(self, i, j):
        self.iCap = i
        self.jCap = j

    def __str__(self):
        return f"{self.iCap}i + {self.jCap}j"


class C3Vector(C2dVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kCap = k

    def __str__(self):
        return f"{self.iCap}i + {self.jCap}j + {self.kCap}k"


v2d = C2dVector(2, 4)
v3d = C3Vector(3, 5, 6)
print(v2d)
print(v3d)