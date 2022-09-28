from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert self.browser.current_url.find("basket") != -1, "URL does not contain 'basket'"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS), \
            "There are some product in the basket, but it should be empty"

    def should_be_text_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_TEXT), "There is no text that basket is empty"