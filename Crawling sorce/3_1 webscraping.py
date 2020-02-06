import webbrowser as wb
# 웹 스크래핑은 웹브라우저 임포트

# 창 띄워주는 코드 wb.open
url = 'www.naver.com'
wb.open(url)

# 자동으로 검색해주는 코드
search_word = "김희지"
# 네이버로 검색
naver_serch_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="
wb.open(naver_serch_url + search_word)
# 구글로 검색
google_serch_url = "https://www.google.com/search?q="
wb.open(google_serch_url + search_word)

#반복문으로 검색
search_words = ['python web scraping','python webbrowser']
for search in search_words:
    wb.open(google_serch_url + search)