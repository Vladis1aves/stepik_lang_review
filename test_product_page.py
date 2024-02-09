import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
import random
import time


@pytest.mark.need_review
class TestGuestAddToBasket:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_empty_basket()

    def test_guest_can_add_product_to_basket(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
        item_page = ProductPage(browser, link)
        item_page.open()
        item_page.should_be_product_page()
        item_page.should_be_message_success_add_to_basket()


@pytest.mark.need_review
class TestGuestGoToLoginPage:
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        time.sleep(3)


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(str(random.randrange(1, 100000))+"vladick@email.com", "123456789Qq")
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        # language = "en-gb"
        link = f"https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
        item_page = ProductPage(browser, link)
        item_page.open()
        item_page.should_be_product_page()
        item_page.should_be_message_success_add_to_basket()


def test_user_cant_see_success_message(browser):
    link = f"https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
    item_page = ProductPage(browser, link)
    item_page.open()
    item_page.not_should_be_alert()


#
# class ProductFactory:
#     link = "link"
#
#     def choice_product(self):
#         pass
#
#     def delete(self):
#         pass
#         #удаляет продукт из корзины
#
#
# @pytest.mark.login_guest
# class TestLoginFromProductPage:
#     @pytest.fixture(scope="function", autouse=True)
#     def setup(self):
#         self.product = ProductFactory(title="Best book created by robot")
#         # создаем по апи
#         self.link = self.product.link
#         yield
#         # после этого ключевого слова начинается teardown
#         # выполнится после каждого теста в классе
#         # удаляем те данные, которые мы создали
#         self.product.delete()
#
#     def test_guest_can_go_to_login_page_from_product_page(self, browser):
#         page = ProductPage(browser, self.link)
#         # дальше обычная реализация теста
#
#     def test_guest_should_see_login_link(self, browser):
#         page = ProductPage(browser, self.link)
#         # дальше обычная реализация теста
