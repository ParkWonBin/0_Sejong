import requests
from bs4 import BeautifulSoup

req = requests.get('https://beomi.github.io/')
html = req.text

soup = BeautifulSoup(html, 'html.parser')


# selector
# HTML : 초보
# CSS : 쉬움, 현업
# CSS가 상위호환 되지만 가끔 안될 때는 다운그레이드 된 것도 알아야 쓸 수 있다.

# partton 확인
my_titles = soup.select(
    'a > h2'
)

# print(my_titles)
# 이렇게 출력하며 태그랑 함께 리스트로 나온다.

for title in my_titles:
    # Tag 안의 텍스트
    print(title.text)
    # 깔끔하게 텍스트 내용만 나온다.

# parser : 번역이란 뜻.