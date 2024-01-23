from selenium.webdriver.common.by import By
import time


def test_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(15)
    browser.implicitly_wait(5)
    button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")
    assert button is not None

