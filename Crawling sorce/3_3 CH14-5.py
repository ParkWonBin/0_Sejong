import requests
from bs4 import BeautifulSoup

# html = requests.get("http://www.naver.com").text

html ="""
<html>
    <body>
        <div>
            <span>
                <a href=http://www.naver.com>네이버</a>
                <a href=http://www.google.com>구글</a>
                <a href=http://www.daum.net>다음</a>
            </span>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html,'lxml')
# lxml은 markup으로 lxml 좀 더 빠른 파서(parser=번역가)다.


print(soup.prettify())
# prettify()는 자동으로 드려쓰기 해주는 메소드.

site_names = soup.find_all('a')
for site_name in site_names :
    print(site_name.get_text())
