# Append to an exesting to the file Pradip.txt 
# it should add data about Pradip's Hometown  

f = open("pradip.txt", "a") 
string = '''
Pradip initially lived in Kolkata WestBengal he is a very nice boy.
'''
f.write(string)

f.close()
