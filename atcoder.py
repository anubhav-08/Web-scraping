import requests
from requests import get
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd 

from time import sleep
from random import randint

# # Initializing storage
# users =[]
problems = []
status =[]
#user and problem finding 
user_id = 'shivam1012'

# problem = 'dp_q'
# solved = False
# Requesting data


headers = {"Accept language" : "en-US, en, q=0.5"}

url = "https://atcoder.jp/contests/dp/submissions?f.Task=&f.LanguageName=&f.Status=&f.User="+user_id

r = requests.get(url)

soup1 = BeautifulSoup(r.text, 'html.parser')


# use for multi page scrapping
if soup1.find('ul', class_='pagination').text != "\n" :
    pages = soup1.find('ul', class_='pagination')
    # print(pages)
else :
    print('User has not solved the problem yet')
    exit()

pages = pages.find_all('li')
pages = int(pages[-1].text)
pages += 1
# print(type(pages))

for page in range(1,pages):

    sleep(randint(2,10))    
    
    r1 = requests.get(url+"&page="+str(page) ,headers=headers)

    soup = BeautifulSoup(r1.text, 'html.parser')
    
    tbody = soup.find('tbody')
    
    rows = tbody.find_all('tr')
    
    # print(len(rows))
    
    for r in rows:
        # Problem
        probAndUser = r.find_all('a')
        # print(probAndUser)
        p = probAndUser[0].get('href') #here p is str type
        p = "https://atcoder.jp"+p
        d = p.split("/")
        p = d[-1]
        problems.append(p)
        # print(p)
        # Status  
        sta = r.find('span', class_='label').text
        status.append(sta)
else:
    table = pd.DataFrame({
        'Problems' : problems,
        'Status' : status
    })


    print(table)

    table.to_csv('atcode.csv')