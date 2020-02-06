import requests
from bs4 import BeautifulSoup

url = "https://music.naver.com/"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")

# "tr td" 이렇게 띄어쓰기를 하면 자동으로 하위 속성을 잡아준다.

# ranking = soup.select('tr._tracklist_move td.name span a')
# 이 코드 문제 : 실시간 1~10, 국내 11~20, 외국 21~30, 리그 31~39 뜬다.

ranking = soup.select('div.tc_panel:first-child td.name span a')
# 첫번 쨰 div(실시간 차트 부분)만 선택한다.

for i in range(1, len(ranking)):
    print(f"{i:2d} : {ranking[i].get_text()}")
# f-string 변수 뒤에 :2d 쓰면 2자리 자연수로 쓴다.

# 이 중 한 가지 패널만 크롤링하도록 할 수 있을까.
