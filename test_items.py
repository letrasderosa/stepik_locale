from selenium.webdriver.common.by import By
import time


lnk = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_buton_present(browser):
    """If only to check the element is present"""
    browser.get(lnk)
    basket = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(basket)>0, "The element is not present"


def test_basket_button_work(browser):
    """The element is displayed and enabled"""
    browser.get(lnk)
    basket = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    time.sleep(4)

    assert basket.is_displayed(), "The element is not displayed"
    print('\nThe element is displayed')
    assert basket.is_enabled(), "The element is not enabled"
    print('The element is enabled')


# pytest --language=es
# pytest --language=en
# pytest --language=ru
# pytest --language=de
# pytest --language=fr
