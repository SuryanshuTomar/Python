class Employee:
    noOfLeaves = 2
    pass


harry = Employee()
harry.salary = 1000
harry.role = "Instructor"

rohan = Employee()
rohan.salary = 500
rohan.role = "Student"

print(harry, rohan)

print(harry.salary)
print(harry.noOfLeaves)
print(rohan.noOfLeaves)

print(Employee.noOfLeaves)
print(rohan.__dict__)
rohan.noOfLeaves = 5
print(rohan.__dict__)
print(Employee.noOfLeaves)
Employee.noOfLeaves = 3
print(Employee.noOfLeaves)
print(Employee.__dict__)
