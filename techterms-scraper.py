import requests
from bs4 import BeautifulSoup
x=input("Enter acronyms : ")
x=x.strip()
x=x.lower()
r = requests.get("http://techterms.com/definition/"+x)
html=r.content
bsObj = BeautifulSoup(html,"html.parser")
bsObj = bsObj.select('article p')
for link in bsObj:
    s=link.get_text()
    if 'Updated:' in s:
        s = s[:s.index('Updated:')]
    print('\n'+s)
