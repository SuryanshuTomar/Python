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


harry = Employee("Harry", 1000, "Instructor")
rohan = Employee("Rohan", 500, "Student")

rohan.changeLeaves(10)
print(Employee.noOfLeaves)

print(rohan.printDetails())
print(harry.printDetails())

# harry = Employee()
# harry.name = "Harry"
# harry.salary = 1000
# harry.role = "Instructor"
#
# rohan = Employee()
# rohan.name = "Rohan"
# rohan.salary = 500
# rohan.role = "Student"
