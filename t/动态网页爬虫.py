from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
url = 'https://www.baidu.com'
browser.get(url)
# print(browser.page_source)
# browser.close()
text=browser.find_element_by_id('wrapper').text
# print(text)
browser.find_element_by_id('kw').send_keys(u'大熊猫')
browser.find_element_by_id('su').click()

time.sleep(2)
browser.save_screenshot("大熊猫.png")


print(browser.get_cookies())

browser.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
browser.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')

browser.find_element_by_id('kw').send_keys(u'老虎')

browser.save_screenshot("老虎.png")
browser.find_element_by_id('su').send_keys(Keys.RETURN)
time.sleep(2)
browser.save_screenshot("老虎2.png")
browser.find_element_by_id('kw').clear()
browser.save_screenshot("clear.png")

browser.quit()