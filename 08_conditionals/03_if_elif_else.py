age = int(input("Enter your age: "))

if(age > 18):
    print("You can drive!")
elif(age == 18):
    print("Lets Sadule a Drive sesion")
elif(age == 0):
    print("New born can drive noob")
elif(age < 0):
    print("Invalid age!")
else:
    print("You can not drive!")