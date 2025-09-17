# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

"""
for i in range(1, 6): # range function excutated n-1 time in this case range(n,n-1) that is range(1, {6-1} = 5) 1 to 5 it print
    print(i)
"""
def numTable(a):
    for i in range(1, 11):
        print(a,"X", i," = ",a*(i))


a = int(input("Enter the table of number: "))
numTable(a)
