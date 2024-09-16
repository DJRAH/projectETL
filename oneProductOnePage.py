import requests
import csv
from bs4 import BeautifulSoup #try to install it if it dosn't done yet
import re #use of pattern to make img's name file clean
import os

def write(link,titleWritten, title, catName):
    url = link #the choosen book  
    print(url)
    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'html.parser')

    desc = soup.find("p", class_ = "")#delect the descrioption of the product
    ths = soup.find_all('th')         #find all description of product's elmnts
    tds = soup.find_all('td')         #find all contents of prodcut's elmnts description
    productTitle = soup.find('h1')         #find all contents of prodcut's elmnts description
    imgUrl = (soup.find('img')['src']).replace('../..','http://books.toscrape.com')#the url of the img in absolute format
    #print('---------url---------'+imgUrl)

    #find titles of product's description
    col = []
    col.append('title')
    for th in ths:
        col.append(th.text)
    col.append('desc')

    #find values of the product's description
    table = []
    table.append(productTitle.text)
    for td in tds:
        table.append(td.text)
    
    if desc:#some product has no description, in this case, we avoid error
        table.append(desc.text)

    #make a imgFileName with use of pattern
    nameImgFile = productTitle.text
    patrn = re.compile('\W')
    nameImgFile = re.sub(patrn, '', nameImgFile) + ".jpg"
    #print(nameImgFile)


    #writing a descriptions's product in a file

    with open('./csvFiles/'+title+'.csv', mode="a", newline="") as csvfile:

        writer = csv.writer(csvfile)
        if titleWritten==0:
            writer.writerow(col)
            if not os.path.isdir('./jpgsFiles/'+catName):
                os.mkdir('./jpgsFiles/'+catName)
        
        writer.writerow(table)

     #saving the img in a desck
    img_data = requests.get(imgUrl).content
    with open('./jpgsFiles/'+catName+'/'+nameImgFile, 'wb') as handler:
        handler.write(img_data) 
