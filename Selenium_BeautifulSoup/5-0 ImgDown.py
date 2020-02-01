import requests
from bs4 import BeautifulSoup
import os

# 왜인지 null 이미지만 저장됨.


# 폴더에 이미지 내려받기
def download_image(img_folder, img_url):
    if img_url is not None:
        html_image = requests.get(img_url)
        # os.path.basename(URL)은 웹사이트나 폴더가 포함된 파일명에서 파일명만 분리
        image_File = open(os.path.join(img_folder, os.path.basename(img_url)), 'wb')

        chunk_size = 1000000000
        # 이미지 데이터를 100000바이트 단위로 저장
        for chunk in html_image.iter_content(chunk_size):
            image_File.write(chunk)
            image_File.close()
        print(f"이미지명 : {os.path.basename(img_url)} 내려받기 완료!")
    else:
        print("내려받을 이미지가 없습니다.")


# 웹사이트 주소 지정:
img_url = "https://image-comic.pstatic.net/nas/user_contents_data/challenge_comic/2019/11/28/khn6918/upload_7292280219508172388.jpeg"

# 이미지 내려받을 폴더 지정
folder=r"C:\Users\Administrator\Desktop\123new"

# 이미지 파일 가져오기

download_image(folder, img_url)
