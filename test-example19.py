import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random

j = 3

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome('C:\\selenium\\chromedriver.exe')
    request.addfinalizer(wd.quit)
    return wd

class CatalogPage:
    def __init__(self, driver):
        self.driver = driver

    def openCatalog(self):
        self.driver.get("http://localhost/litecart/en/")
        return self

    def openProduct(self):
        allProducts = self.driver.find_elements_by_css_selector("[id=box-most-popular] li.product")
        index = random.randint(0, len(allProducts) - 1)
        go = allProducts[index].find_element_by_xpath("./a[@class='link']").click()

class CartElement:
    def __init__(self, driver):
        self.cart_element = driver.find_element_by_css_selector("#cart-wrapper")

    def go_cart(self):
        self.cart_element.find_element_by_css_selector("[href*=checkout]").click()

class ProductElement:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def inCart(self):
        return self.driver.find_element_by_xpath("//span[@class='quantity']")

    def add_to_cart(self):
        self.product = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#box-product")))[0]
        try:
            self.product.find_element_by_css_selector("[name='options[Size]']").click()
            self.product.find_element_by_css_selector("[name='options[Size]'] [value='Small']").click()
            self.product.find_element_by_name("add_cart_product").click()
        except Exception:
            self.product.find_element_by_name("add_cart_product").click()
        newCount = int(self.inCart.text) + 1
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class='quantity']"), str(newCount)))

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def remove_all_products(self):
        thtabel = self.driver.find_element_by_css_selector("[class='quantity']")
        for i in range(j):
            self.driver.find_element_by_name("remove_cart_item").click()
            self.wait.until(EC.staleness_of(thtabel))

def test_cart(driver):
    for i in range(j):
        CatalogPage(driver).openCatalog().openProduct()
        ProductElement(driver).add_to_cart()
    CartElement(driver).go_cart()
    CartPage(driver).remove_all_products()

