"""Employee Class"""


class Employee:
    def __init__(self, first_name, last_name, age, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.pay = pay
        self.email = f"{self.first_name}.{self.last_name}@email.com"

    def fullname(self):
        return f"{self.first_name} {self.last_name}"


emp_1 = Employee("Mawulorm", "Agbodeka", 25, 6000)

# Testing concepts
print("---", emp_1.fullname())
print(emp_1.first_name)

print(Employee.fullname(emp_1))
