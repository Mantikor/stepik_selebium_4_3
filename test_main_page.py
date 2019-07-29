import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage


@pytest.mark.login_guest
class TestLoginFromMainPage(object):

    def test_guest_can_go_to_login_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/we-are-anonymous_192/'
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/we-are-anonymous_192/'
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_should_see_login_page_forms(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_not_be_product_in_basket()
    cart_page.should_be_message_about_empty_basket()
