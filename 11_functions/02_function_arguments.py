def add(a, b, plus = 0):
    x = a + b + plus
    return x


c1 = add(5, 3, 50) # Default Argument
print(c1)
c2 = add(
    b = 15,
    plus = 50,
    a = 44 
) # Keyword Argument
print(c2)
