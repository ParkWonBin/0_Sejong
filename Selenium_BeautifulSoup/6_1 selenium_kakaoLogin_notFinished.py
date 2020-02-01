from selenium import webdriver
import time



driver = webdriver.Chrome('C:/chromedriver')

driver.implicitly_wait(1)

url = 'https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net%252F'
driver.get(url)
time.sleep(2)

check = 'recaptcha-checkbox-border'

driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]').click()

# driver.find_element_by_name('email').send_keys(id)

# driver.find_element_by_name('password').send_keys(pw)

# driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span/input').click()
