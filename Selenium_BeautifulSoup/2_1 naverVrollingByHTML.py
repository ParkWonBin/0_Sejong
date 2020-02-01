import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.naver.com/')
html = req.text
soup = BeautifulSoup(html,"html.parser")

title = soup.find(id="PM_ID_serviceNavi")
print(title.text)

