import pytest
import random
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome('C:\\selenium\\chromedriver.exe')
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/en/")
    wait = WebDriverWait(driver, 10)
    j=3

    for i in range(j):
        products = driver.find_elements_by_css_selector("[id=box-most-popular] li.product")
        index = random.randint(0, len(products) - 1)
        inPurchaseCart = driver.find_element_by_css_selector("[class=quantity]").get_attribute("textContent")
        newCount = int(inPurchaseCart)+1
        go = products[index].find_element_by_xpath("./a[@class='link']").click()
        try:
            driver.find_element_by_css_selector("[name='options[Size]']").click()
            driver.find_element_by_css_selector("[name='options[Size]'] [value='Small']").click()
            driver.find_element_by_name("add_cart_product").click()
        except Exception:
            driver.find_element_by_name("add_cart_product").click()

        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class='quantity']"), str(newCount)))
        driver.get("http://localhost/litecart/en/")

    driver.find_element_by_css_selector("[href*=checkout]").click()
    thtabel = driver.find_element_by_css_selector("[class='quantity']")
    for i in range(j):
        driver.find_element_by_name("remove_cart_item").click()
        wait.until(EC.staleness_of(thtabel))
