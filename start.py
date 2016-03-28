import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

LOGIN_URL = 'https://app.pluralsight.com/id?redirectTo=%252Ftraining'
LOGIN = None
PASSWORD = None

def login(url):
    """
    Login to the site
    """
    driver = webdriver.Chrome()
    driver.get(url)

    elem = driver.find_element_by_name('Username')
    elem.send_keys(LOGIN)

    elem = driver.find_element_by_name('Password')
    elem.send_keys(PASSWORD)

    elem = driver.find_element_by_id('login')
    elem.click()

    return driver

def get_all_links(driver, url):
    """
    Get all the video page links
    """
    driver.get(url)
    link_list = driver.find_elements_by_class_name('table-of-contents__clip-list-title')

    return link_list

def download_link(driver, link):
    """
    Given a link, download the file
    """
    link_str = str(link.get_attribute('href'))
    print link_str

    driver.get(link_str)

    elem = driver.find_element_by_class_name('vjs-tech')

    video_link = str(elem.get_attribute('src'))

    new_file_name = video_link.split('/')[6] + '.mp4'
    print new_file_name

    # download video link
    # urllib.urlretrieve(video_link, new_file_name)

    # rename video to new file name
    i = 3

def run():

    url = "https://app.pluralsight.com/library/courses/raspberry-pi-home-server/table-of-contents"

    driver = login(LOGIN_URL)

    link_list = get_all_links(driver, url)

    for link in link_list:
        download_link(driver, link)

    driver.close()

if __name__ == '__main__':
    run()