import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://www.yandex.com/")
    driver.find_element_by_name("text").send_keys("webdriver")
    driver.find_element_by_class_name("search2__button").click()
    WebDriverWait(driver, 10)
