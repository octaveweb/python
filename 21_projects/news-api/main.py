import requests
topic= str(input("Search here any topic: "))
api = "cf49c648111543eb87de761f421c0736"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2025-08-27&to=2025-08-27&sortBy=popularity&apiKey={api}"
print(url)

r = requests.get(url)
print(r)
data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1,article['title'])
    print(article['url'])
    print("\n*****************************************\n")

