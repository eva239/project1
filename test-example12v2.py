import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import os

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome('C:\\selenium\\chromedriver.exe')
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    driver.find_element_by_link_text("Add New Product").click()

    driver.find_element_by_css_selector("[href*='#tab-general']").click()
    WebDriverWait(driver, 10)
    if not driver.find_element_by_name("status").is_selected():
        driver.find_element_by_name("status").click()
    nameproduct = "New Product 15"
    driver.find_element_by_name("name[en]").send_keys(nameproduct)
    driver.find_element_by_name("code").send_keys("123-123-123")
    driver.find_element_by_css_selector("[name='categories[]'][value='2']").click()
    driver.find_element_by_css_selector("[name='product_groups[]'][value='1-3']").click()
    driver.find_element_by_name("quantity").clear()
    driver.find_element_by_name("quantity").send_keys("10")
    filename = "/product.png"
    root_path = os.path.dirname(__file__)
    abs_path = root_path + filename
    filepath = os.path.abspath(abs_path)
    driver.find_element_by_name("new_images[]").send_keys(filepath)
    driver.find_element_by_css_selector("#add-new-image").click()
    driver.find_element_by_name("date_valid_from").click()
    driver.find_element_by_name("date_valid_from").send_keys('01-01-2018')
    driver.find_element_by_name("date_valid_to").click()
    driver.find_element_by_name("date_valid_to").send_keys('31-12-2018')

    driver.find_element_by_css_selector("[href*='#tab-information']").click()
    WebDriverWait(driver, 10)
    if not driver.find_element_by_css_selector("[name='manufacturer_id']").is_selected():
        driver.find_element_by_css_selector("[name='manufacturer_id'] [value = '1']").click()
    driver.find_element_by_name("keywords").send_keys("new good product")
    driver.find_element_by_name("short_description[en]").send_keys("Buy this new product.")

    driver.find_element_by_css_selector("[href*='#tab-prices']").click()
    WebDriverWait(driver, 10)
    driver.find_element_by_name("purchase_price").clear()
    driver.find_element_by_name("purchase_price").send_keys("5")
    driver.find_element_by_name("purchase_price_currency_code").click()
    driver.find_element_by_name("purchase_price_currency_code").send_keys("EUR")
    driver.find_element_by_name("prices[EUR]").send_keys("10")

    driver.find_element_by_name("save").click()
    driver.find_element_by_id("content").click()
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    driver.find_element_by_link_text(nameproduct).click()