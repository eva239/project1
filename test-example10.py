import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome('C:\\selenium\\chromedriver.exe')
#    wd = webdriver.Firefox(firefox_binary="c:\\Program Files\\Mozilla FirefoxESR\\firefox.exe")
#    wd = webdriver.Ie('C:\\selenium\\IEDriverServer.exe')
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def transf_digits(size):
    size = str(size)
    size = size.replace("px", "")
    size = size.replace("[", "")
    size = size.replace("]", "")
    size = size.replace("'", "")
    return size

def rgbchanel(color):
    color = str(color)
    color = color.replace("(", "")
    color = color.replace(")", "")
    color = color.replace(", ", ",")
    color = color.replace("'", "")
    color = color.replace("[", "")
    color = color.replace("]", "")
    color = color.replace("rgba", "")
    color = color.replace("  ", "")
    return color

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
    SalePriceProduct_color = []
    n_SalePriceProduct_color = []
    SalePriceProductTag = []
    n_SalePriceProductTag = []

    i=0
    for product in products:
        count.append(i)
        linkProducts.append(product.find_element_by_css_selector("[class='link']").get_attribute('href'))
        productName.append(product.find_element_by_css_selector("[class='name']").text)
        product_price.append(product.find_element_by_css_selector("[class='price-wrapper'] [class='regular-price']").text)
        SalePriceProduct.append(product.find_element_by_css_selector("[class='price-wrapper'] [class='campaign-price']").text)

        SalePriceProduct_color.append(product.find_element_by_css_selector("[class='price-wrapper'] [class='campaign-price']").value_of_css_property('color'))
        SalePriceProduct_color = rgbchanel(SalePriceProduct_color)
        SalePriceProduct_color = SalePriceProduct_color.split(",")
        gchanelSalePriceProduct = SalePriceProduct_color[1]
        bchanelSalePriceProduct = SalePriceProduct_color[2]
        SalePriceProductTag.append(product.find_element_by_css_selector("[class='price-wrapper'] [class='campaign-price']").get_attribute('outerHTML'))
        PriceProduct_text.append(product.find_element_by_css_selector("[class='price-wrapper'] [class='regular-price']").value_of_css_property('text-decoration'))
        PriceProduct_color.append(product.find_element_by_css_selector("[class='price-wrapper'] [class='regular-price']").value_of_css_property('color'))
        PriceProduct_color = rgbchanel(PriceProduct_color)
        PriceProduct_color = PriceProduct_color.split(",")
        rchanelPriceProduct = PriceProduct_color[0]
        gchanelPriceProduct = PriceProduct_color[1]
        bchanelPriceProduct = PriceProduct_color[2]
        PriceProduct_font_size.append(product.find_element_by_css_selector("[class='price-wrapper'] [class='regular-price']").value_of_css_property('font-size'))
        SalePriceProduct_font_weight.append(product.find_element_by_css_selector("[class='price-wrapper'] [class='campaign-price']").value_of_css_property('font-weight'))
        SalePriceProduct_font_size.append(product.find_element_by_css_selector("[class='price-wrapper'] [class='campaign-price']").value_of_css_property('font-size'))
        print("")
        print('В каталоге:', productName, product_price, SalePriceProduct, SalePriceProduct_color, PriceProduct_text, PriceProduct_color, PriceProduct_font_size, SalePriceProduct_font_weight, SalePriceProduct_font_size)
        i+=1

    for j in range(len(count)):
        driver.get(linkProducts[j])
        n_productName = driver.find_element_by_css_selector("[id='box-product'] [class='title']").text
        n_product_price = driver.find_element_by_css_selector("[id='box-product'] [class = 'regular-price']").text
        n_SalePriceProduct = driver.find_element_by_css_selector("[id='box-product'] [class = 'campaign-price']").text
        n_SalePriceProduct_color = driver.find_element_by_css_selector("[class='price-wrapper'] [class='campaign-price']").value_of_css_property('color')
        n_SalePriceProduct_color = rgbchanel(n_SalePriceProduct_color)
        n_SalePriceProduct_color = n_SalePriceProduct_color.split(",")
        gchanel_n_SalePriceProduct = n_SalePriceProduct_color[1]
        bchanel_n_SalePriceProduct = n_SalePriceProduct_color[2]
        n_SalePriceProductTag.append(driver.find_element_by_css_selector("[class='price-wrapper'] [class='campaign-price']").get_attribute('outerHTML'))
        n_PriceProduct_text=driver.find_element_by_css_selector("[id='box-product'] [class = 'regular-price']").value_of_css_property('text-decoration')
        n_PriceProduct_color = driver.find_element_by_css_selector("[id='box-product'] [class = 'regular-price']").value_of_css_property('color')
        n_PriceProduct_color = rgbchanel(n_PriceProduct_color)
        n_PriceProduct_color = n_PriceProduct_color.split(",")
        rchanel_n_PriceProduct = n_PriceProduct_color[0]
        gchanel_n_PriceProduct = n_PriceProduct_color[1]
        bchanel_n_PriceProduct = n_PriceProduct_color[2]
        n_PriceProduct_font_size=driver.find_element_by_css_selector("[id='box-product'] [class = 'regular-price']").value_of_css_property('font-size')
        n_SalePriceProduct_font_weight=driver.find_element_by_css_selector("[id='box-product'] [class='campaign-price']").value_of_css_property('font-weight')
        n_SalePriceProduct_font_size=driver.find_element_by_css_selector("[id='box-product'] [class='campaign-price']").value_of_css_property('font-size')
        print('Детали товара:', n_productName, n_product_price, n_SalePriceProduct, n_SalePriceProduct_color, n_PriceProduct_text,n_PriceProduct_color, n_PriceProduct_font_size, n_SalePriceProduct_font_weight, n_SalePriceProduct_font_size)

    assert n_productName == productName[j]
    assert n_product_price == product_price[j]
    assert n_SalePriceProduct == SalePriceProduct[j]

#цена обычная зачеркнутая
    assert "line-through" in PriceProduct_text[j]
    assert "line-through" in n_PriceProduct_text

# проверка: обычная цена - серая (в каталоге и деталях)
    assert rchanelPriceProduct == gchanelPriceProduct
    assert gchanelPriceProduct == bchanelPriceProduct
    assert rchanel_n_PriceProduct == gchanel_n_PriceProduct
    assert gchanel_n_PriceProduct == bchanel_n_PriceProduct

# цена акционная жирная
    SalePriceProductTag = str(SalePriceProductTag)
    n_SalePriceProductTag = str(n_SalePriceProductTag)
    assert "strong" in SalePriceProductTag
    assert "strong" in n_SalePriceProductTag

# проверка: акционная цена - красная (в каталоге и деталях)
    assert gchanelSalePriceProduct[j] == bchanelSalePriceProduct[j]
    assert gchanelSalePriceProduct[j] == '0'
    assert gchanel_n_SalePriceProduct == bchanel_n_SalePriceProduct
    assert gchanel_n_SalePriceProduct == '0'

#акционная цена крупнее, чем обычная
    PriceProduct_font_size = transf_digits(PriceProduct_font_size)
    n_PriceProduct_font_size = transf_digits(n_PriceProduct_font_size)
    SalePriceProduct_font_size = transf_digits(SalePriceProduct_font_size)
    n_SalePriceProduct_font_size = transf_digits(n_SalePriceProduct_font_size)
    assert PriceProduct_font_size < SalePriceProduct_font_size
    assert n_PriceProduct_font_size < n_SalePriceProduct_font_size




