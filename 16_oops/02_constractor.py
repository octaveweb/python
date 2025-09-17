class Employye:
    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name = name
        self.bond =bond
    
    def get_salary(self): # self is importent it reference the object that has been created 
        return self.salary
       
    def get_info(self):
        print(f"The name of the Empolyee is {self.name}. His salary is {self.salary}. The bond is for {self.bond} years")
# e1 = Employye(
#     name="Karan Swarnakar",
#     salary=150000,
#     bond= "15 years"
# )
e1 = Employye(50000, "Karan", 4)
# print(e1.get_salary())
print(e1.get_info())

