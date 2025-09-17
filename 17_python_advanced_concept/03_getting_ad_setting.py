class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @property
    def first_name(self):
        l = self.name.split(" ") 
        # print(l) # ['Karan', 'Swarnakar']
        # print(l[0])
        # print(l[1])
        return l[0]
    
    @first_name.setter
    def first_name(self, name):
    # def set_first_name(self, name):
        l = self.name.split(" ")
        # print(l)
        new_name = f"{name} {l[1]}"
        self.name = new_name



    
e1 = Employee("Karan Swarnakar", 505000)
# print(e1.name)
# print(e1.salary)

# e1.project = 5
# print(e1.project)

# print(e1.first_name()) 
# e1.set_first_name("Sonu")
# print(e1.name)

print(e1.first_name)
e1.first_name = "Sonu"
print(e1.name)





