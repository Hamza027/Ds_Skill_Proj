from selenium import webdriver
from curses.ascii import BEL
from email import header
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re




def extract(i,what,where):
    headers = {"USer:Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
    url = f"https://uk.indeed.com/jobs?q={what}&l={where}&start={i}&vjk=d0cef20b803f0a29"
    
    #r = requests.get(url,headers)
    driver.get(url)
    driver.implicitly_wait(2)
    r = driver.find_element_by_id("resultsBodyContent")
    soup = BeautifulSoup(r.get_attribute("innerHTML"),'html.parser')
    #print({"R status code":r.status_code})
    #print(soup)

    transform(soup)

def transform(soup):
    Href = []
    Company = []
    Title = []
    
    for ref in soup.findAll("a", class_=re.compile("tapItem fs-unmask result job_\d*")):

        if ref.get('href') == None:
            #for i in range (0,15):
                Href.append("Nan")
        else:
            Href.append("https://uk.indeed.com"+ ref['href'])
        
            
     
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
            
    # Error handling for Href Tag
    if len(Href) == 0:
        for i in range(len(Company)):
            Href.append("Nan")
    
    load(Title,Company,Href)
    print({"Title":len(Title),"Company":len(Company),"Link":len(Href)},"\n")


def load(Title,Company,Href):
    df = pd.DataFrame({"Title":Title,"Company":Company,"Link":Href})
    df.to_csv("Jobs_links.csv", mode='a', header=False, index=False)


driver = webdriver.Chrome("./chromedriver")


what = input("Enter the job title you are looking for: ")
where = input("Enter location you are looking for: ")


for i in range(0,321,10):
    #print(f"\n{i}")
    extract(i,what,where)