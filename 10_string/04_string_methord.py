# name = "Karan" # String are immutable

# name[0] = "A" # Run time error Can not change

# a = len(name)
# print(a)

# s = "hello world"
# print("Original: ", s)
# print("UpperCase: ",s.upper())
# print("LowerCase",s.lower())
# print("Capitalize",s.capitalize())
# print("Capitalize",s.title())


text1 = " hello world "
print(text1.strip()) # Output: "hello world"
print(text1.lstrip()) # Output: "hello world "
print(text1.rstrip()) # Output: " hello world"


text2 = "Python is fun"
print(text2.find("is")) # Output: 7
print(text2.replace("fun", "awesome")) # Output: "Python is awesom


text3 = "Apple, Banana, Greaps, Orenge"
print(text3.split(","))
print(",".join(['Apple', ' Banana', ' Greaps', ' Orenge']))


text4 = "Python123"
print(text4.isalpha()) # Output: False
print(text4.isdigit()) # Output: False
print(text4.isalnum()) # Output: True
print(text4.isspace()) # Output: False
