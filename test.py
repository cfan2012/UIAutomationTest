from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def open_browser(path):
    s = Service(path)
    driver = webdriver.Chrome(service=s)
    return driver


def close_browser(driver):
    driver.quit()


def test_view_page():
    webdriver_path = './chromedriver'
    driver = open_browser(webdriver_path)
    driver.get("https://www.baidu.com/")
    assert "百度一下，你就知道" in driver.title
    close_browser(driver)


if __name__ == '__main__':
    test_view_page()
