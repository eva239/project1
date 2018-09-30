import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome('C:\\selenium\\chromedriver.exe')
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    menuQty = driver.find_elements_by_id("app-")
    for i in range(len(menuQty)):
        menu = driver.find_elements_by_id("app-")
        menu[i].click()
        WebDriverWait(driver, 10)
        submenuQty = driver.find_elements_by_css_selector("[id^=doc-]")
        if len(submenuQty)<1:
            driver.find_element_by_css_selector("h1")
        for j in range(len(submenuQty)):
            submenu = driver.find_elements_by_css_selector("[id^=doc-]")
            submenu[j].click()
            driver.find_element_by_css_selector("h1")