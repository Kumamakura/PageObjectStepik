from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.url.find("login"), "URL is not correct"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        input_password.send_keys("123456789!")
        input_password_confirm = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM)
        input_password_confirm.send_keys("123456789!")
        button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION_SUBMIT)
        button.click()


