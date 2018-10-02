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
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    WebDriverWait(driver, 10)

    idCountries = []
    rows = driver.find_elements_by_xpath(".//table[@class='dataTable']//tr[@class='row']")
    i = 0
    for elements in rows:
        column = elements.find_elements_by_tag_name("td")
        idCountries.append(column[1].text)
        i += 1
    for id in idCountries:
        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=edit_geo_zone&page=1&geo_zone_id="+str(id))
        countriesList = []
        countries = driver.find_elements_by_css_selector("[id=table-zones] td:nth-child(3) [selected=selected]")
        for i in range(len(countries)-1):
            countriesList.append(countries[i].text)
        print(countriesList)
        sortedCountries = sorted(countriesList)
        assert countriesList == sortedCountries

