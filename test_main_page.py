from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import pytest


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_empty_basket()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product = "the-girl-who-played-with-non-fire_203"
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/" + product
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_empty_basket()


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_should_see_login_link(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()         # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        page.should_be_login_link()      # проверим что тест выдаст ошибку на неправильный селектор



