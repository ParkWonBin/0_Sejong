from selenium import webdriver
import time

# ====================================
id = "########"
pw = "********"
# ====================================
driver = webdriver.Chrome('C:/chromedriver')

driver.get('https://nid.naver.com/nidlogin.login?url=http%3A%2F%2Fmail.naver.com%2F')
driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
driver.find_element_by_class_name("btn_global").click()


#
# from bs4 import BeautifulSoup
#
# driver.get('https://mail.naver.com')
#
# html = driver.page_source
# soup = BeautifulSoup(html, 'lxml')
#
#
# sendlist = soup.find_all('div', 'name _ccr(lst.from) ')
#
# [s.extract() for s in soup('span', {'class':'blind'})]
# titlelist = soup.find_all('div', 'subject')
#
# for i in range(len(sendlist)):
#     print(sendlist[i].find('a').get_text())
#     print(titlelist[i].find('strong').get_text())
#     print()
