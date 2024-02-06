from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_empty_basket(self):
        basket_empty = self.find(*BasketPageLocators.empty_basket)
        assert str(basket_empty.text).split(".")[0] == "Your basket is empty", f"Text not correctly: {basket_empty.text}"
        self.items_to_buy_now_not_present()

    def items_to_buy_now_not_present(self):
        assert self.is_not_element_present(*BasketPageLocators.basket_items_to_buy_now)

