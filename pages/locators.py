from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_INVALID')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini a')
    BASKET_BUTTON_INVALID = (By.CSS_SELECTOR, '.basket-mini_inc')


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, '#registration_link')


class LoginPageLocators(object):
    REGISTER_INPUT_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_INPUT_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_INPUT_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON_REGISTER = (By.CSS_SELECTOR, 'button[name=registration_submit]')
    LOGIN_INPUT_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_INPUT_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON_LOGIN = (By.CSS_SELECTOR, 'button[name=login_submit]')


class CartPageLocators(object):
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, '.basket-items h3')
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner p')


class ProductPageLocators(object):
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
