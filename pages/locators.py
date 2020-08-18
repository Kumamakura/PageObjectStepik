from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION_SUBMIT = (By.CSS_SELECTOR, '[name = "registration_submit"]')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    MESSAGE_BASKET_ADDED = (By.CSS_SELECTOR, ".alert-success > .alertinner strong")
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info > .alertinner strong")


class BasePageLocators:
    BUTTON_LINK_TO_BASKET = (By.CSS_SELECTOR, '.btn-group > .btn[href *= "basket"]')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
