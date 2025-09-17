class Employee:
    company = "HP"

    def get_salary(self): # self is importent it reference the object that has been created 
        print(self)
        return 50000
    
e = Employee() # An Object Employee is created 
print(e.get_salary()) # Employee Salary methord is called

e2 = Employee()
print(e2.get_salary())