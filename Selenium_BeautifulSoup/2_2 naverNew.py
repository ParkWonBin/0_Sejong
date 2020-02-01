# 뉴스 롤링페이지 크롤링

import urllib.request
from bs4 import BeautifulSoup as bs

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)
# print(html)

bs_obj = bs(html, "html.parser")
# print( bs_obj )
ol = bs_obj.find("ol", {"class": "ca_l"})

#  하위 리스트 를 넣는다.
lists = ol.find_all("li")

for li in lists:
    # a 태그를 찾는다.
    a_tag = li.find("a")
    print(a_tag.text)

# ================
# import requests
# from bs4 import BeautifulSoup
#
# req = requests.get("https://naver.com")
# html = req.text
# soup = BeautifulSoup(html,"html.parser")
#
# news = soup.select(".cast_atc _PM_newsstand_rolling")
# print(news)
#
# for i in range(4):
#     print(i)
