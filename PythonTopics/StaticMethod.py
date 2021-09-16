class Employee:
    company = "Google"

    def getSalary(self):
        print(f"Salary of employee working in {self.company} is {self.salary}")

    # when we don't want to create a method without passing the self argument instance
    # Then we will use the @staticmethod decorator
    @staticmethod
    def greet():
        print("Hello Everyone")


shanky = Employee()
shanky.salary = "$250K"
shanky.getSalary()  # can also be written as -> Employee.getSalary(shanky)
shanky.greet()
