import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import random

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome('C:\\selenium\\chromedriver.exe')
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10)
    mail_random=random.randint(99,999999)
    password = '1234567'
    driver.find_element_by_css_selector("[name='login_form'] [href*='create_account']").click()
    driver.find_element_by_name("tax_id").send_keys("1")
    driver.find_element_by_name("company").send_keys("2")
    driver.find_element_by_name("firstname").send_keys("Иванов")
    driver.find_element_by_name("lastname").send_keys("Сергей")
    driver.find_element_by_name("address1").send_keys("город, улица, дом, 1")
    driver.find_element_by_name("address2").send_keys("город, улица, дом, 2")
    driver.find_element_by_name("postcode").send_keys("23901")
    driver.find_element_by_name("city").send_keys("New York")
    driver.find_element_by_name("country_code").send_keys("United States")
    driver.find_element_by_name("email").send_keys("user"+str(mail_random)+"@yandex.ru")
    mailrandom = "user"+str(mail_random)+"@yandex.ru"
    driver.find_element_by_name("phone").send_keys("1234567")
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("confirmed_password").send_keys(password)
    WebDriverWait(driver, 100)
    driver.find_element_by_name("create_account").send_keys(Keys.ENTER)
    driver.find_element_by_name("zone_code").send_keys("Alaska")
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("confirmed_password").send_keys(password)
    driver.find_element_by_name("create_account").send_keys(Keys.ENTER)

    driver.find_element_by_link_text("Logout").click()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("email").send_keys(mailrandom)
    driver.find_element_by_name("login").click()
    driver.find_element_by_link_text("Logout").click()

