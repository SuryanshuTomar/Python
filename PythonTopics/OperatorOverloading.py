class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, otherInstance):
        print("let's Add")
        return self.num + otherInstance.num

    def __mul__(self, otherInstance):
        print("let's Multiply")
        return self.num * otherInstance.num


n1 = Number(4)
n2 = Number(6)

# In Operator overloading, whenever we perform any arithmetic operations on the
# class objects, we can define also how we want to perform operation on these objects
# using predefined dunder method like in this case use are using __add__ and  __mul__.
adding = n1 + n2
print(adding)
multiplying = n1 * n2
print(multiplying)


class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} "
            index += 1
        return str1[:-1]

    def __add__(self, other):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + other.vec[i])
        return Vector(newList)

    def __mul__(self, other):
        addingProd = 0
        for i in range(len(self.vec)):
            addingProd += (self.vec[i] * other.vec[i])
        return addingProd


v1 = Vector([1, 4, 7])
v2 = Vector([2, 5, 8])
print(v1 + v2)
print(v1 * v2)

