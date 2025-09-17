def marks(**kwargs):
    for item in kwargs.keys():
        print(f"the marks of {item} are {kwargs[item]}")


marks(karan = 50, pradip = 50, jesmine = 71, payal = 45)
