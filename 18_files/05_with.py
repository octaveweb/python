"""
f = open("karan.txt", "r")
content = f.read()
print(content)
"""

with open("karan.txt", "r") as f:
    content = f.read()
    print(content)
    # No need to f.close() becouse by defult it is close when using {with syntex}