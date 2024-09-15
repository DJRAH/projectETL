import requests
import csv
from bs4 import BeautifulSoup #try to install it if it dosn't done yet

def write(link,titleWritten, title):
    url = link #the choosen book  
    print(url)
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
    
    if desc:#some product has no description, in this case, we avoid error
        table.append(desc.text)



    #writing in a file

    with open(title+'.csv', mode="a", newline="") as csvfile:

        writer = csv.writer(csvfile)
        if titleWritten==0:
            writer.writerow(col)
        
        writer.writerow(table)

        
        

