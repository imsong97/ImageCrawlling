import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://search.naver.com/search.naver?where=image&section=blog&query=%EC%9B%83%EB%8A%94%20%EC%97%B0%EC%98%88%EC%9D%B8%20%EC%96%BC%EA%B5%B4&res_fr=0&res_to=0&sm=tab_opt&face=1&color=0&ccl=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&datetype=0&startdate=0&enddate=0&start=1"

CHROME_DRIVER = "/Users/yunho/Downloads/chromedriver"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
image = soup.find_all("img", {"class": "_img"}, limit=2)

n = 1

for i in image:
  imgUrl = i['data-source']
  with urlopen(imgUrl) as f:
    with open("naver"+str(n)+'.jpg','wb') as h: # w - write b - binary
      img = f.read()
      h.write(img)
  print(str(n)+"번 사진 완료")
  n += 1

# def viewMore():
#   driver = webdriver.Chrome(CHROME_DRIVER)
#   driver.get(url)
#   driver.find_element_by_xpath("//a[@class='btn_more _more']").click()
#   res = driver.find_element_by_xpath("//div[@class='photo_grid _box']")
#   print(res)