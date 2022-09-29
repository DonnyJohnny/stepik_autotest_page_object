from selenium.webdriver.common.by import By


class BasePageLocators():    
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group>a.btn-default")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_TEXT = (By.CSS_SELECTOR, "div#content_inner>p")
    PRODUCTS = (By.CSS_SELECTOR, "form#basket_formset")

class LoginPageLocators():
    EMAIL_INPUT = (By.CSS_SELECTOR, "form#register_form input#id_registration-email")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "form#register_form input#id_registration-password2")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "form#register_form input#id_registration-password1")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "form#register_form>button")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")    

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")    
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main>p.price_color")
    PRICE_IN_BASCET = (By.CSS_SELECTOR, "div.alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success strong")