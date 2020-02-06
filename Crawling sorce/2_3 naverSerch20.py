import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.find("ul", {"class":"ah_l"})
lis = ul.findAll("li")

for li in lis:
    rank = li.find("span",{"class":"ah_r"})
    a = li.find("span", {"class":"ah_k"})
    print(str(rank.text) + ". " + str(a.text))