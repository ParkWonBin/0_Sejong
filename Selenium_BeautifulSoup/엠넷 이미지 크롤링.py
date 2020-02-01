import bs4
import requests

def save_image(img_url, date, rank, title, artist):
    response = requests.get(img_url)
    content = response.content
    filename = "{}\\{:03}_{}_{}.jpeg".format(date, rank, title, artist)
    file = open(filename,"wb")
    file.write(content)

date = input("검색할 날짜[YYYYmmdd]를 입력하세요 : ")
pages = int(input("총 몇 페이지를[50/page]를 크롤링할까요 : "))

charts = []
for page in range(1, pages + 1):
    url = "http://www.mnet.com/chart/TOP100/{}?pNum={}".format(date, page)
    response = requests.get(url)
    text = response.text
    html = bs4.BeautifulSoup(text, "html.parser")

    tr_list = html.find("table").find("tbody").find_all("tr")
    for tr in tr_list:
        rank = int(tr.find("span", {"class": "MMLI_RankNum"}).text.rstrip("위"))
        img_url = tr.find("img")["src"]
        title = tr.find("a", {"class": "MMLI_Song"}).text
        try:
            artist = tr.find("a", {"class": "MMLIInfo_Artist"}).text
            album = tr.find("a", {"class": "MMLIInfo_Album"}).text
        except:
            artist_album = tr.find("div", {"class": "MMLITitle_Info"}).text
            artist = artist_album.split("/")[0].strip("\n\t\r ")
            album = artist_album.split("/")[1].strip("\n\t\r ")

        charts.append([rank, title, artist, album, img_url])

import csv
import os
command = "md {}".format(date)
os.system(command)
filename = "{}\\charts-{}.csv".format(date, date)
file = open(filename, "w", newline="", encoding="utf-8-sig")
csvfile = csv.writer(file)

for song in charts:
    rank = song[0]
    title = song[1]
    artist = song[2]
    img_url = song[-1]
    save_image(img_url, date, rank, title, artist)
    csvfile.writerow(song[:-1])

file.close()