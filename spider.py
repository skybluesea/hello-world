from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html, "lxml")
rsp = soup.find_all("tr", id = "gift1")
for i in rsp:
    print(type(i))
    print(i.img["src"])