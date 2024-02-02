from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    register_form = (By.CSS_SELECTOR, '#register_form')
    login_form = (By.CSS_SELECTOR, '#login_form')


class ItemPageLocators:
   basket_form = (By.CSS_SELECTOR, '#add_to_basket_form')
   item_title = (By.CSS_SELECTOR, 'div[class*="product_main"] h1')
   button_basket = (By.CSS_SELECTOR, '#add_to_basket_form button[type="submit"]')
