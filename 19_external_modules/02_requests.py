import requests

r = requests.get('https://api.github.com/users/octaveweb')

# print(r.text)
with open("octaveweb.txt", "w") as f:
    f.write(r.text)