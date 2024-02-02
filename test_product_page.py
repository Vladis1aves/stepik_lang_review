from .pages.product_page import ItemPage


def test_add_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    item_page = ItemPage(browser, link)
    item_page.open()
    item_page.should_be_product_page()


