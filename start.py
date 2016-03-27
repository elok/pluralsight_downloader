from selenium import webdriver
from selenium.webdriver.common.keys import Keys

password = None

driver = webdriver.Chrome()
driver.get("https://app.pluralsight.com/library/courses/raspberry-pi-home-server/table-of-contents")

elem = driver.find_element_by_name('Username')
elem.send_keys('ericlok@gmail.com')

elem = driver.find_element_by_name('Password')
elem.send_keys(password)

elem = driver.find_element_by_id('login')
elem.click()

link_list = driver.find_elements_by_class_name('table-of-contents__clip-list-title')

for link in link_list:
    link_str = str(link.get_attribute('href'))
    print link_str

driver.close()