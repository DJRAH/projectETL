import requests
import csv
from bs4 import BeautifulSoup #try to install it if it dosn't done yet

url = "http://books.toscrape.com/catalogue/the-secret-of-dreadwillow-carse_944/index.html" #the choosen book  

res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

desc = soup.find("p", class_ = "")#delect the descrioption of the product
ths = soup.find_all('th')         #find all description of product's elmnts
tds = soup.find_all('td')         #find all contents of prodcut's elmnts description

#find elmnts of product's description
col = []
for th in ths:
    #print(th.text)
    tl = th.text
    col.append(tl)

#constitute a table of the product's description
table = []
i=0
for td in tds:
    #print(th.text)
    ct = td.text
    el = [col[i],ct]
    table.append(el)
    i+=1



#writing in a file

with open('oneProductExtracted.csv', mode="w", newline="") as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(['desc\t'+desc.text])
    for el in table:
        writer.writerow([el[0]+'\t'+el[1]])
    csvfile.close()
    
