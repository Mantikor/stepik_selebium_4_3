import pytest
import time
from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage


class TestUserAddToCartFromProductPage(object):

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        email = str(time.time()) + '@fakemail.org'
        password = 'let2be_a-paSSwOrD'
        page = LoginPage(self.browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/we-are-anonymous_192/'
        page = ProductPage(self.browser, link)
        page.open()
        page.press_button_add_to_basket()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/we-are-anonymous_192/'
        page = ProductPage(self.browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/we-are-anonymous_192/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_not_be_product_in_basket()
    cart_page.should_be_message_about_empty_basket()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/we-are-anonymous_192/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_dissapeared_after_adding_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/we-are-anonymous_192/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
