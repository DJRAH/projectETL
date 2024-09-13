import requests
import csv
from bs4 import BeautifulSoup #try to install it if it dosn't done yet
import oneProductOnePage

url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html" #the choosen book  
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

desc = soup.find_all("img")#recover all tags with links

#constitue all links
links=[]
for im in desc:
    al = str((im.parent)['href'])
    link = 'https://books.toscrape.com/catalogue/' + al.removeprefix("../../../")
    links.append(link)

#write all product of the category to a file
i=0
for li in links:
    oneProductOnePage.write(li,i)
    i=1


    