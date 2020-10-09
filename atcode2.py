# code to check whether user has solved particular problem or not

import requests
from requests import get
from bs4 import BeautifulSoup


# Details given
user_id = 'anubhav'
problem = 'dp_b'
solved = False
# Requesting data


headers = {"Accept language" : "en-US, en, q=0.5"}

url = f"https://atcoder.jp/contests/dp/submissions?f.Task={problem}&f.LanguageName=&f.Status=AC&f.User={user_id}"

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')

if(soup.find('tbody')):
    print("YES (Yes a correct solution found")
else:
    print("NO (This user has not solved this problem yet")


