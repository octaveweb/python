numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1st Approch

# def square(x):
#     return x*x

# new = list(map(square, numbers))
# print("Origanal: ",numbers)
# print("Map: ",new)


# 2nd Approch 
new = list(map(lambda x: x*x, numbers)) # lambda function
print("Origanal: ",numbers)
print("Map: ",new)