from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):

    def should_be_message_about_empty_basket(self):
        empty_text = self.browser.find_element(*CartPageLocators.BASKET_EMPTY_TEXT).text
        assert empty_text == 'Your basket is empty. Continue shopping', 'Text about empty basket not present'

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_PRODUCT_NAME), 'Name of product present, but should not be'
