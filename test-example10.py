import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver(request):
#    wd = webdriver.Chrome('C:\\selenium\\chromedriver.exe')
    wd = webdriver.Firefox(firefox_binary="c:\\Program Files\\Mozilla FirefoxESR\\firefox.exe")
#    wd = webdriver.Ie('C:\\selenium\\IEDriverServer.exe')
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10)
    products = driver.find_elements_by_css_selector("[id=box-campaigns] li.product")

    count=[]
    linkProducts=[]
    productName=[]
    product_price=[]
    SalePriceProduct=[]
    PriceProduct_text=[]
    PriceProduct_color = []
    PriceProduct_font_size=[]
    SalePriceProduct_font_weight=[]
    SalePriceProduct_font_size=[]

    i=0
    for product in products:
        count.append(i)
        linkProducts.append(product.find_element_by_css_selector("[class='link']").get_attribute('href'))
        productName.append(product.find_element_by_css_selector("[class='name']").text)
        product_price.append(product.find_element_by_css_selector("[class='price-wrapper'] [class='regular-price']").text)
        SalePriceProduct.append(product.find_element_by_css_selector("[class='price-wrapper'] [class='campaign-price']").text)
        PriceProduct_text.append(product.find_element_by_css_selector("[class='price-wrapper'] [class='regular-price']").value_of_css_property('text-decoration'))
        PriceProduct_color.append(product.find_element_by_css_selector("[class='price-wrapper'] [class='regular-price']").value_of_css_property('color'))
        PriceProduct_font_size.append(product.find_element_by_css_selector("[class='price-wrapper'] [class='regular-price']").value_of_css_property('font-size'))
        SalePriceProduct_font_weight.append(product.find_element_by_css_selector("[class='price-wrapper'] [class='campaign-price']").value_of_css_property('font-weight'))
        SalePriceProduct_font_size.append(product.find_element_by_css_selector("[class='price-wrapper'] [class='campaign-price']").value_of_css_property('font-size'))
        print("")
        print('В каталоге:', productName, product_price, SalePriceProduct, PriceProduct_text, PriceProduct_color, PriceProduct_font_size, SalePriceProduct_font_weight, SalePriceProduct_font_size)
        i=i+1

    for j in range(len(count)):
        driver.get(linkProducts[j])
        n_productName = driver.find_element_by_css_selector("[id='box-product'] [class='title']").text
        n_product_price=driver.find_element_by_css_selector("[id='box-product'] [class = 'regular-price']").text
        n_SalePriceProduct=driver.find_element_by_css_selector("[id='box-product'] [class = 'campaign-price']").text
        n_PriceProduct_text=driver.find_element_by_css_selector("[id='box-product'] [class = 'regular-price']").value_of_css_property('text-decoration')
        n_PriceProduct_color = driver.find_element_by_css_selector("[id='box-product'] [class = 'regular-price']").value_of_css_property('color')
        n_PriceProduct_font_size=driver.find_element_by_css_selector("[id='box-product'] [class = 'regular-price']").value_of_css_property('font-size')
        n_SalePriceProduct_font_weight=driver.find_element_by_css_selector("[id='box-product'] [class='campaign-price']").value_of_css_property('font-weight')
        n_SalePriceProduct_font_size=driver.find_element_by_css_selector("[id='box-product'] [class='campaign-price']").value_of_css_property('font-size')

    print('Детали товара:', n_productName, n_product_price, n_SalePriceProduct, n_PriceProduct_text,n_PriceProduct_color, n_PriceProduct_font_size, n_SalePriceProduct_font_weight, n_SalePriceProduct_font_size)

    assert n_productName == productName[j]
    assert n_product_price == product_price[j]
    assert n_SalePriceProduct == SalePriceProduct[j]
    assert n_PriceProduct_text == PriceProduct_text[j]
    assert n_PriceProduct_color == PriceProduct_color[j]
    assert n_PriceProduct_font_size == PriceProduct_font_size[j]
    assert n_SalePriceProduct_font_weight == SalePriceProduct_font_weight[j]
    assert n_SalePriceProduct_font_size == SalePriceProduct_font_size[j]