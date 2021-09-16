class Employee:
    noOfLeaves = 5

    # Constructor
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    # Object Method
    def printDetails(self):
        return f"The name is {self.name}. Salary is {self.salary}. And role is {self.role}"

    # Class Method
    @classmethod
    def changeLeaves(cls, leaves):
        cls.noOfLeaves = leaves

    # Class Method as an Alternate Constructor
    @classmethod
    def fromString(cls, string):
        return cls(*string.split("-"))
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])


harry = Employee("Harry", 1000, "Instructor")
rohan = Employee("Rohan", 500, "Student")
karan = Employee.fromString("Karan-1500-Senior Instructor")

print(karan.salary, karan.role)
rohan.changeLeaves(10)
print(Employee.noOfLeaves)

print(rohan.printDetails())
print(harry.printDetails())
