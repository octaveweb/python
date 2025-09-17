def sum(a, b):
    return a + b


print(sum(500, 15)) 
# print(sum(500, 15, 85)) # can't give 3 argument it will throw an error

def any_num_sub(*args):
    # print(args)
    total = 0
    for item in args:
        total += item
    return total

print(any_num_sub(2,3,5,8,5,8,5,14))



