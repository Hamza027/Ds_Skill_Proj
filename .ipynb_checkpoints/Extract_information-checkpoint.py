from curses.ascii import BEL
from email import header
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


def extract(i):
    headers = {"USer:Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
    url = f"https://uk.indeed.com/jobs?q=Data%20Scientist&l=United%20Kingdom&start={i}&vjk=d0cef20b803f0a29"
    
    r = requests.get(url,headers)
    soup = BeautifulSoup(r.content,'html.parser')

    transform(soup)

def transform(soup):
    Href = []
    Company = []
    Title = []  
    for ref in soup.findAll("a",href=True, class_="tapItem"):
        Href.append(ref['href'])
     
    for item in soup.findAll('h2',{'class':'jobTitle'}):
        title = item.find_all('span')
        if(len(title)==2):
            Title.append(title[1].text)
        else:
            Title.append(title[0].text)

    comp = soup.findAll('div',{'class':'heading6 company_location tapItem-gutter companyInfo'})
    for item in comp:
        
        if item.span.a == True:
            Company.append(item.span.find('a', class_ = 'turnstileLink companyOverviewLink').text)
        else:
            Company.append(item.find('span', class_ = 'companyName').text)
    
    load(Title,Company,Href)


def load(Title,Company,Href):
    print(len(Title),len(Company),len(Href))
    df = pd.DataFrame({"Title":Title,"Company":Company,"Link":Href})
    df.to_csv("data.csv", mode='a', header=False, index=False)


for i in range(0,101,10):
    extract(i)
    time.sleep(2)

df = pd.read_csv("data.csv")
df.head(10)











