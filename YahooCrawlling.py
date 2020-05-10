import requests
from urllib.request import urlopen
import urllib.error
from bs4 import BeautifulSoup

url = "https://images.search.yahoo.com/search/images;_ylt=Awr9DWuW.LRezoUAoPaJzbkF?p=smile+human+face&ei=UTF-8&y=Search&fr=yfp-t-s&imgty=photo&fr2=p%3As%2Cv%3Ai"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

image = soup.find_all("img", {"class": "process"})

n = 1

for i in image:
    imgUrl = i['data-src']
    try:
        with urlopen(imgUrl) as f:
            with open("yahoo"+str(n)+'.jpg','wb') as h:
                img = f.read()
                h.write(img)
    except urllib.error.URLError as e: print(e)
    print(str(n)+"번 사진 완료")
    n += 1

