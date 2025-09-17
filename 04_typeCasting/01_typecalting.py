
"""
ease to use 
    also can use as 
        a= 15
        print(a, "Typeof")
        print(type(a))
        print(" ")
"""
def printItDataType(a):
    print(a, "Typeof")
    print(type(a))
    print(" ")


a = 10
b = "55"
d = 223


printItDataType(a)
printItDataType(b)

# Convert b to an integer
c = int(b) # type castin to int 
printItDataType(c)

e = str(d)
printItDataType(e)