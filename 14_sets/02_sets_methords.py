s = {1,55,6,62,81,83,64,24,41,8}
print(s)
s.add(45)
print(s)
s.remove(1)
print(s)
# s.remove(100) # Throw an error
s.discard(100)  # If present then remove and listen don't throw any error
print(s)