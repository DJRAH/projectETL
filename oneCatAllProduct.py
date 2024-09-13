import requests
import csv
from bs4 import BeautifulSoup #try to install it if it dosn't done yet

url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html" #the choosen book  
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

desc = soup.find_all("img")#recover all tags with links

links=[]

for im in desc:
    al = str((im.parent)['href'])
    link = 'http://books.toscrape.com/catalogue/category/books/' + al.removeprefix("../../../")
    links.append(link)

for li in links:
    print(li)