import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

#class MyListener(AbstractEventListener):
#    def before_find(self, by, value, driver):
#        print(by, value)
#    def after_find(self, by, value, driver):
#        print(by, value, "found")
#    def on_exception(self, exception, driver):
#        print(exception)

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome('C:\\selenium\\chromedriver.exe')
 #   wd = EventFiringWebDriver(wd, MyListener())
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    wait = WebDriverWait(driver, 10)
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    links = []
    products = driver.find_elements_by_css_selector("[name=catalog_form] [class=row] [href*='edit_product']")
    for i in range(len(products)):
        links.append(products[i].get_attribute("href"))

    for i in range(len(products)):
        href = links[i]
        print("Товар:",href)
        driver.get(href)
        for l in driver.get_log("browser"):
            if l == "":
                print("ошибок нет")
            else:
                print("ошибка:",l)
        driver.find_element_by_name("cancel").click()