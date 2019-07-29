import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Choose language')


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # chrome_d_path = '/opt/Chrome/chromedriver'
    # browser = webdriver.Chrome(options=options, executable_path=chrome_d_path)
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
