import requests # pip install requests

req = requests.get('https://beomi.github.io/') # 이 사이트를 크롤링한다.
# print(req) # http 상태코드 (200 정상, 404 오류)

html = req.text
# print(html) # 해당 사이트의 html 전체코드

# 전체 크롤링은 이렇게 쓰는 게 끝이다.
# 이제 전체 영역에서 원한느 부분만 뽑기아내자.

headers = req.headers
# print(headers) # 해더 정보값을 알려준다.

status = req.status_code
# print(status)

is_ok = req.ok
# print(is_ok) # 사이트 정상 운영 중이면 TURE 나옴

if req.ok:
    print("https://beomi.github.io/ 사이트 정상 운영 중")
else:
    print("깨짐")

