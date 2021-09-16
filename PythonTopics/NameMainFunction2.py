def printSomething(string):
    return print(f"This is a simple string statement {string}")


def addNumber(num1, num2):
    return print(num1 + num2)


print("The name is :", __name__)

if __name__ == '__main__':
    addNumber(7, 8)
    printSomething("DeathSlayer")
