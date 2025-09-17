class Employee:
    company = "Google"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self): # made for the user to see  
        l = self.name.split(" ")
        # print(l)
        return f"Mr.{l[0]} Is the HR, and his salary is {self.salary}"
    
    def __repr__(self): # made for the devepoper to see 
        # print(l)
        return f"Name:{self.name}\nSalary:{self.salary}"

    def __len__(self):
        return len(self.name)

    def info_print(self):
        print("Name:", self.name)
        print("Salary:",self.salary)

e = Employee("Karan Swarnakar", 45000)
print(len(e))
# e.info_print()
# print(str(e))
# print(repr(e))