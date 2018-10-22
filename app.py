import requests
from bs4 import BeautifulSoup as bs4


query = input("Enter query : ") 
LINK = f"https://www.amazon.in/s/ref=nb_sb_noss?field-keywords={query}"

r = requests.get(LINK)

soup = bs4(r.text, "html.parser")

items = soup.findAll("div", {"class" : "s-item-container"})

#txtData = [" ".join([i.strip() for i in item.text.strip().split(" ")]) for item in items]
#for data in txtData:
#    print(data)

#print(items[3])

for item in items[1:len(items)-1]:
    try:
        title = item.findChild("h2", {"class" : "s-access-title"}).text.strip()
        ilink = item.findChild("a", {"class" : "s-access-detail-page"}).get("href")
        price = item.findChild("span", {"class" : "s-price"}).text.strip()
        rating = item.findChild("i", {"class" : "a-icon-star"}).text.strip()
        print(title, ilink, price, rating, sep="\n")
        print("\n")
    except Exception as e:
        pass
