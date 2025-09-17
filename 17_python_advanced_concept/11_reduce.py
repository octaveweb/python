from functools import reduce 

a = [1, 2, 3, 4, 5, 6]
def sum(a,b):
    return a + b

new = reduce(sum, a )
print(new)



