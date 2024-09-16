import requests
import csv
from bs4 import BeautifulSoup #try to install it if it dosn't done yet
import oneProductOnePage

def extractAllProductsOfCategory(aurl, title):
    url = "http://books.toscrape.com/"+aurl #the url of the category
    print(url)
    catName = ((aurl.split('/')[3]).split('_')[0])
    print("------------------------- url of a category ---------------------------")
    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'html.parser')

    desc = soup.find_all("img")#recover all tags with links

    next = soup.find("li", class_="next")

    #recover all page's link of the category
    i=1
    urlsCat = []#contains all url of the product's category
    urlsCat.append(url)

    #check if there's a next button, some add others urls to the category list's links
    while next:
        linkNext = (next).a['href']
        newLink = url[:url.rfind('/')]+'/'+linkNext
        urlsCat.append(newLink)
        #check if the nextpage of the category contains another next
        pres = requests.get(newLink)
        psoup = BeautifulSoup(pres.text, 'html.parser')
        next = psoup.find("li", class_="next")


    #recover all links for all product of the category
    links=[]#contains all product url ot the category
    for lin in urlsCat:
        print(lin)
        res = requests.get(lin)
        soup = BeautifulSoup(res.text, 'html.parser')
        desc = soup.find_all("img")#recover all tags with links


        for im in desc:
            al = str((im.parent)['href'])
            link = 'https://books.toscrape.com/catalogue/' + al.removeprefix("../../../")
            links.append(link)
    
    print('-------------------------------------------------------------------------------------------------------')
    print(len(links))
    print('-------------------------------------------------------------------------------------------------------')

    for li in links:
        print(li) 

    #write all product of the category to a file
    i=0
    for li in links:
        oneProductOnePage.write(li,i,title, catName)
        i=1


        