from .pages.product_page import ItemPage
import time


def test_add_to_basket(browser):
    # language = "en-gb"
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    item_page = ItemPage(browser, link)
    item_page.open()
    item_page.should_be_product_page()
    item_page.should_be_message_success_add_to_basket()
    time.sleep(3)
