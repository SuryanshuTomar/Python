class Employee:
    company = "Google"
    salary = 200
    location = "California"

# This will change the instance level attribute salary
# and not the class salary of the Employee class
#     def changeSalary(self, salary):
#         self.salary = salary

# If you want to change the class level attribute of the Employee class then,
# one method is you can use Dunder/magic class methods.
#     def changeSalary(self, salary):
#         self.__class__.salary = salary

# Another method to change the class level attribute are using class methods.
# and instead of passing the instance, pass the class "cls"
# This will change the class level attribute salary and not instance attribute
    @classmethod
    def changeSalary(cls, salary):
        cls.salary = salary


e = Employee()
print(e.salary)
e.changeSalary(455)
print(Employee.salary)
