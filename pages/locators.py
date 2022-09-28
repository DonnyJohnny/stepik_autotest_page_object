from selenium.webdriver.common.by import By


class BasePageLocators():    
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group>a.btn-default")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    EMPTY_TEXT = (By.CSS_SELECTOR, "div#content_inner>p")
    PRODUCTS = (By.CSS_SELECTOR, "form#basket_formset")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success>strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main>h1")