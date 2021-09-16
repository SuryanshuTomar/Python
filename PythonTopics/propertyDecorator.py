class Employee:
    company = "Google"
    salary = 1000000
    salaryBonus = 210000

    # This is also called Getter method
    # So, this will be treated as a property as all other getter methods are treated
    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus

    # This is also called Setter method and this will set the property values
    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 2500000
print(e.salary)
print(e.salaryBonus)

