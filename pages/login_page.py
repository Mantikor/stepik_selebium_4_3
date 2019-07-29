from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert 'login' in url, 'Not login page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT_EMAIL), 'Login input email not present'
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT_PASSWORD), 'Login input password not present'
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON_LOGIN), 'Login button not present'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_INPUT_EMAIL), 'Registation email not present'
        assert self.is_element_present(*LoginPageLocators.REGISTER_INPUT_PASSWORD), 'Registration password not present'
        assert self.is_element_present(*LoginPageLocators.REGISTER_INPUT_PASSWORD_CONFIRM), 'Confirmation password not present'
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON_REGISTER), 'Register button not present'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON_REGISTER).click()
