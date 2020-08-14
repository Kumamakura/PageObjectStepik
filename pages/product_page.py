from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_correct_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_BASKET_ADDED), "Message basket added is not presented"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_basket_added = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_ADDED).text
        assert product_name in message_basket_added, "The product name does not equal the name in the message."

    def should_be_correct_product_price_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_PRICE), "Message basket sum is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        basket_price = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price in basket_price, "The product price does not equal the basket price."
