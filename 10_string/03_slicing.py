name = "Karan0123456789"

print(name[0:2]) # gose from 0 to 2-1 i.e {K,a}
print(name[2:-1]) # name[2: (-1 + lenth of String ie 5) so 4] name[2,4-1] ie name[2,3] {ra}

print("Skip slice on string")
print("--------------------")
# print(name[0:10:n-1]) # Skilp 'n-1' charaters
print("Original:",name,"\n")
print("Skip '0' charaters:",name[0:10:1])
print("Skip '1' charaters:",name[0:10:2]) 
print("Skip '2' charaters:",name[0:10:3]) 
print("Skip '3' charaters:",name[0:10:4]) 

text = "Hello, Python!"
print(text[0:5]) # Output: Hello
print(text[:5]) # Output: Hello
print(text[7:]) # 
print(text[0:]) # 
