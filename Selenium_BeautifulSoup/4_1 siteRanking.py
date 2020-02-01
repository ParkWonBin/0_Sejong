import requests
from bs4 import BeautifulSoup

url = "https://www.alexa.com/topsites/countries/KR"

html_web_ranking = requests.get(url).text
soup_web_ranking = BeautifulSoup(html_web_ranking,"lxml")

# p 태그의 요소 안에서 a 태그의 요소를 찾음
web_ranking = soup_web_ranking.select('p a')

for i in range(1,10):
    print(f"{i} : {web_ranking[i].get_text()}")
