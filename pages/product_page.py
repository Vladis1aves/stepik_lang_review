from .base_page import BasePage
from .locators import ItemPageLocators
import time


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_basket_button()
        self.should_be_item_name()

    def should_be_message_success_add_to_basket(self):
        self.should_be_basket_clickbait()
        self.solve_quiz_and_get_code()
        self. should_be_equivalently_total_and_product_price()
        self. should_be_equivalently_name_product()

    def should_be_product_url(self):
        assert self.browser.current_url == self.url, f"Incorrect item url, factual {self.browser.current_url}, actual {self.url}"

    def should_be_basket_button(self):
        assert self.is_element_present(*ItemPageLocators.basket_form), "Basket button is not presented"

    def should_be_basket_clickbait(self):
        basket_button = self.find(*ItemPageLocators.button_basket)
        basket_button.click()
        alert = self.browser.switch_to.alert
        assert alert is not None

    def should_be_item_name(self):
        assert self.is_element_present(*ItemPageLocators.item_title), "Title item is not presented"

    def should_be_equivalently_total_and_product_price(self):
        basket_total = str(self.find(*ItemPageLocators.basket_total).text).split()[-3]
        product_price = str(self.find(*ItemPageLocators.price_incl_tax).text)
        assert basket_total == product_price, f"Price is not equivalently {basket_total} and {product_price}"

    def should_be_equivalently_name_product(self):
        name_product = self.find(*ItemPageLocators.item_title).text
        name_product_in_basket = str(self.find(*ItemPageLocators.title_product_in_basket).text)
        assert name_product == name_product_in_basket, "Name is not equivalently"

    def not_should_be_alert(self):
        assert self.is_not_element_present(*ItemPageLocators.title_product_in_basket), "Alert is success"

    def element_is_not_disappeared(self):
        assert self.is_disappeared(*ItemPageLocators.title_product_in_basket), "Element is Disappeared"
