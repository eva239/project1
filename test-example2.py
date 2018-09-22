import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
    #chrome_driver = webdriver.Chrome()
    #ie_driver = webdriver.Ie()
    #firefox_driver = webdriver.Firefox()

    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    WebDriverWait(driver, 10)

