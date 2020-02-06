import requests
from bs4 import BeautifulSoup

# html = requests.get("http://www.naver.com").text

html2 ="""
<html>
    <head>
        <title> 작품과 작가 모음</title>
    </head>
    <body>
        <h1>책 정보</h1>
        <p id = "book_title">토지</p>
        <p id = "author">박경희</p>

        <p id = "book_title">감옥으로부터의 사색</p>
        <p id = "author">신영복</p>

       
    </body>
</html>
"""

soup2 = BeautifulSoup(html2,'lxml')
# lxml은 markup으로 lxml 좀 더 빠른 파서(parser=번역가)다.
print(soup2.title.text)
print(soup2.body.text)
print(soup2.body.h1.text)
print(soup2.find_all("p"))
print("==============")


titles = soup2.find_all('p',{"id":"book_title"})
authors = soup2.find_all('p',{"id":"book+author"})

# 이거 왜 안돼지?
for title, author in zip(titles,authors):
    print(title.get_text())
    print(author.get_text())

for title in titles:
    print(title.get_text())