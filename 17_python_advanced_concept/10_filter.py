
# 1st Approch
# def greater_then_10(x):
#     if x > 10:
#         return True
#     else:
#         return False
    
# a = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# new = list(filter(greater_then_10, a))
# print("Ogiginal: ",a)
# print("Filter: ",new)



# 2nd Approch
    
a = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

new = list(filter(lambda x: x>10, a))
print("Ogiginal: ",a)
print("Filter: ",new)