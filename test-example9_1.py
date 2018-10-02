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
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    WebDriverWait(driver, 10)

    #пункт а
    countriesList = driver.find_elements_by_css_selector("[href*=country_code]:not([title='Edit'])")
    countries = []
    for i in range(len(countriesList)):
        countries.append(countriesList[i].text)
    sortedCountries = sorted(countries)
    assert countries == sortedCountries


    #пункт б
    codeCountries=[]
    rows = driver.find_elements_by_xpath(".//table[@class='dataTable']//tr[@class='row']")
    i = 0
    for elements in rows:
        column = elements.find_elements_by_tag_name("td")
        if int(column[5].text) > 0:
            codeCountries.append(column[3].text)
            i += 1
    for code in codeCountries:
        driver.get("http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code="+str(code))
        countriesList2 = []
        countries = driver.find_elements_by_css_selector("[id=table-zones] tr td:nth-child(3)")
        for i in range(len(countries)-1):
            countriesList2.append(countries[i].text)
        sortedCountries2 = sorted(countriesList2)
        assert countriesList2 == sortedCountries2