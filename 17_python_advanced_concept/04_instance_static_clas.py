class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_info(self):
        info = f"Emplyee: {self.name} \nSallary:{self.salary}"
        print(info)

    # Static Methord
    @staticmethod
    def sum(a, b):
        return a + b
    
    # Class Methord
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


print(Employee.company)

e1 = Employee("Karan Swarnakar", 49999)
# print(e1.company)
# print(e1.name)
# print(e1.salary)

e1.print_info()

e2 = Employee("Pradip Biswas", 49999)
# print(e2.company)
# print(e2.name)
# print(e2.salary)

e2.print_info()

print(e1.sum(45, 40))

# instance Have change
e2.print_company()
e2.change_company("Google")
e2.print_company()
# Chaking Class Company name change or not
Employee.print_company() # Google
# Bravo! it change 