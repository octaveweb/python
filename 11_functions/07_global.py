def sum (a,b):
    print("Hay Karan Whatapp!")
    c = a + b
    global z # plz modify globle z
    z = 0
    return c

z = 3
print(sum(3, 12))
print(z)