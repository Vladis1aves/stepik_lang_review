from .base_page import BasePage
from .locators import ItemPageLocators


class ItemPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_basket_button()
        self.should_be_item_name()

    def should_be_product_url(self):
        assert self.browser.current_url == self.url, f"Incorrect item url, factual {self.browser.current_url}, actual {self.url}"

    def should_be_basket_button(self):
        assert self.is_element_present(*ItemPageLocators.basket_form), "Basket button is not presented"

    def should_be_item_name(self):
        assert self.is_element_present(*ItemPageLocators.item_title), "Title item is not presented"
