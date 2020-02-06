import requests
from bs4 import BeautifulSoup

req = requests.get('https://naver.com')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

ul = soup.select('.an_txt')

title_result = []

for title in ul:
    title_result.append(title.text)

print(title_result)
print(title_result[0:7])
print(title_result[7:])


# ================
# # 직접 해보기
# import requests
# from bs4 import BeautifulSoup
#
# req = requests.get('https://www.naver.com/')
# html = req.text
# soup = BeautifulSoup(html,"html.parser")
#
# ul = soup.select('.an_txt')
# for i in range(7):
#     print(ul[i].text)
