template = "Dear {} you are the greatest in the world. Take this {}$"
a = "Jon" 
a1 = 100
b = "Motu"
b1 = 1000
c = "Putlu"
c1 = 1000
d = "Gasita Ram"
d1 = 800
e = "Jatka"                    
e1 = 800

s1 = template.format(a,a1) 
s2 = template.format(b,b1)
s3 = template.format(c,c1)
s4 = template.format(d,d1)
s5 = template.format(e,e1)
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

print(f"{a} you are great and take this {a1}$") # direct variable inject (NEW)