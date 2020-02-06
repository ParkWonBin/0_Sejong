import requests
from bs4 import BeautifulSoup
import os

# 왜인지 null 이미지만 저장됨.
# 1화에서 82화까지 자동저장해주는 코드로 만듬.


# 이미지 추출 함수 정의
def get_image_url(url):
    html_image = requests.get(url).text
    soup_image = BeautifulSoup(html_image, "lxml")
    # image_elements = soup_image.select('td a img')
    image_elements = soup_image.select('div.wt_viewer img')
    # image_elements = soup_image.select('img')

    if image_elements is not None:
        image_urls = []
        for image_element in image_elements:
            image_urls.append(image_element.get('src'))
    return image_urls


# 폴더에 이미지 내려받기
def download_image(img_folder, img_url):
    if img_url is not None:
        html_image = requests.get(img_url)
        # os.path.basename(URL)은 웹사이트나 폴더가 포함된 파일명에서 파일명만 분리
        image_File = open(os.path.join(img_folder, os.path.basename(img_url)), 'wb')

        chunk_size = 10000000000
        # 이미지 데이터를 100000바이트 단위로 저장
        for chunk in html_image.iter_content(chunk_size):
            image_File.write(chunk)
            image_File.close()
        print(f"이미지명 : {os.path.basename(img_url)} 내려받기 완료!")
    else:
        print("내려받을 이미지가 없습니다.")

# 이미지 내려받을 폴더 지정
folder=r"C:\Users\Administrator\Desktop\123new"

# 해당 만화 1화에서 82화까지 다운받는 코드
for i in range(1,82):

    # 웹사이트 주소 지정:
    img_url = f"https://comic.naver.com/bestChallenge/detail.nhn?titleId=721777&no={i}"

    # 이미지 파일 가져오기
    img_urls = get_image_url(img_url)

    # 다운받을 이미지 개수
    num_of_download = len(img_urls)

    for k in range(num_of_download):
        download_image(folder, img_urls[k])
