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
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10)
    products = driver.find_elements_by_id("li.product")
    for product in products:
        stickers = product.find_elements_by_css_selector("li.product .sticker")
        assert len(stickers) == 1