import requests
import csv
from bs4 import BeautifulSoup #try to install it if it dosn't done yet
import oneCatAllProduct 

url = "http://books.toscrape.com" #the choosen book  
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
desc = soup.find_all("a")

#recover all urls of categories

categoriesUrl=[]#contains all urls of categories
for el in desc:
    lin = el['href']
    if lin.startswith("catalogue/category/books/"):
        categoriesUrl.append(lin)
        

#for each category, extract all products category in csv file named as the title of category
for link in categoriesUrl:
    title=((((str(link).split('/'))[3])).split('_'))[0]
    oneCatAllProduct.extractAllProductsOfCategory(link, title)

