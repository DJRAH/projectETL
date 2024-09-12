import requests
import csv
from bs4 import BeautifulSoup #try to install it if it dosn't done yet

url = "http://books.toscrape.com/catalogue/the-secret-of-dreadwillow-carse_944/index.html" #the choosen book  
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

desc = soup.find("p", class_ = "")#delect the descrioption of the product
ths = soup.find_all('th')         #find all description of product's elmnts
tds = soup.find_all('td')         #find all contents of prodcut's elmnts description

#find titles of product's description
col = []
for th in ths:
    col.append(th.text)
col.append('desc')

#find values of the product's description
table = []

for td in tds:
    table.append(td.text)
table.append(desc.text)



#writing in a file

with open('oneProductExtracted.csv', mode="w", newline="") as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(col)
    writer.writerow(table)

    csvfile.close()
    

