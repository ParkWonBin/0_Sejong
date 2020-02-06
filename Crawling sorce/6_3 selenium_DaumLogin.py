from selenium import webdriver

# 다음 로그인
driver = webdriver.Chrome('c:/chromedriver')
driver.implicitly_wait(3)

driver.get('https://logins.daum.net/accounts/toploginform.do')
driver.find_element_by_name('id').send_keys('****')
driver.find_element_by_id('inputPwd').send_keys('****')
driver.find_element_by_xpath('//*[@id="loginSubmit"]').click()

driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div[2]/ul/li[1]/em/a').click()

senders = driver.find_elements_by_css_selector("a.link_from")
titles = driver.find_elements_by_css_selector("strong.tit_subject")

for sender, title in zip(senders,titles):
    sender_result = sender.text
    title_result = title.text
    # print(sender_result)
    # print(title_result)
    print("{0} : {1}".format(sender_result, title_result))

driver.quit()