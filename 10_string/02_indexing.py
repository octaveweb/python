name = "Karan"
# name = " K  a  r  a  n"
#          0  1  2  3  4
#         -5 -4 -3 -2 -1

print(name[0]) # {K}
print(name[1]) # {a}
print(name[2]) # {r}
print(name[3]) # {a}
print(name[4]) # {n}

print(name[-1]) # {n}
print(name[-2]) # {a}
print(name[-3]) # {r}
print(name[-4]) # name[-4+5] that is name[1] # {a}
print(name[-5]) # {K}

# for i in range(1, 6):
    # print(name[i-1])