from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import time
import pytest


@pytest.mark.skip
@pytest.mark.parametrize('link', ["promo=offer0",
                                  # "promo=offer1",
                                  # "promo=offer2",
                                  # "promo=offer3",
                                  # "promo=offer4",
                                  # "promo=offer5",
                                  # "promo=offer6",
                                  # "promo=offer7",
                                  # "promo=offer8",
                                  # "promo=offer9"
                                  ])
def test_add_to_basket(browser, link):
    # language = "en-gb"
    LINK = f"https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?{link}"
    item_page = ProductPage(browser, LINK)
    item_page.open()
    item_page.should_be_product_page()
    item_page.should_be_message_success_add_to_basket()
    time.sleep(3)


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    LINK = f"https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
    item_page = ProductPage(browser, LINK)
    item_page.open()
    item_page.should_be_message_success_add_to_basket()
    item_page.not_should_be_alert()
    time.sleep(2)


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    LINK = f"https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
    item_page = ProductPage(browser, LINK)
    item_page.open()
    item_page.not_should_be_alert()
    time.sleep(2)


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    LINK = f"https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
    item_page = ProductPage(browser, LINK)
    item_page.open()
    item_page.should_be_message_success_add_to_basket()
    item_page.element_is_not_disappeared()
    time.sleep(2)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

