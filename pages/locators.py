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
   price_incl_tax = (By.CSS_SELECTOR, "div table tbody tr:nth-child(4) td")
   basket_total = (By.CSS_SELECTOR, 'div.basket-mini.pull-right.hidden-xs')
   title_product_in_basket = (By.CSS_SELECTOR, 'div#messages div:nth-child(1) div strong')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    basket_button = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs a.btn.btn-default")


class BasketPageLocators:
    empty_basket = (By.CSS_SELECTOR, "div.content div#content_inner p")
    basket_items_to_buy_now = (By.CSS_SELECTOR, "div.content div#content_inner div.basket-title.hidden-xs")


