from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS), "The basket should be empty, but there are items in it."

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), "Empty basket text is not presented"
