import requests
from urllib.request import urlopen
import urllib.error
from bs4 import BeautifulSoup

url = "https://www.bing.com/images/search?&q=웃는+연예인+얼굴&qft=+filterui:face-face&FORM=IRFLTR"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

image = soup.find_all("a", {"class": "thumb"})

n = 1

for i in image:
    imgUrl = i['href']
    try:
        with urlopen(imgUrl) as f:
            with open("msn"+str(n)+'.jpg','wb') as h:
                img = f.read()
                h.write(img)
    except urllib.error.URLError as e: print(e)
    print(str(n)+"번 사진 완료")
    n += 1

