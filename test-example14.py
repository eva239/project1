import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome('C:\\selenium\\chromedriver.exe')
#    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    WebDriverWait(driver, 10)
    driver.find_element_by_link_text("Add New Country").click()
    Links = driver.find_elements_by_css_selector("form tbody tr td i")

    for i in range(len(Links)):
        print("Переход по ссылке",i+1)
        Links[i].click()
        WebDriverWait(driver, 20).until(EC.number_of_windows_to_be(2))
        AllOpenWindows = driver.window_handles
        currentWindow = driver.current_window_handle
        oldWindow=currentWindow
        print("текущее окно:", currentWindow)

        for j in range(len(AllOpenWindows)):
            if (AllOpenWindows[j] != currentWindow):
                newWindow = AllOpenWindows[j]
                print("новое окно:",newWindow)
        driver.switch_to.window(newWindow)

        currentWindow = driver.current_window_handle
        print("перешли в окно:", currentWindow)
        driver.close()
        driver.switch_to.window(oldWindow)
        currentWindow = driver.current_window_handle
        print("вернулись в старое окно:", currentWindow)
    driver.quit()