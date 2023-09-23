import pytest
from selene.support.shared import browser
from selene import browser


@pytest.fixture(autouse=True)
def open_browser():
    browser.open('https://google.com')


@pytest.fixture(scope='function', autouse=True)
def config_browser():
    browser.driver.set_window_size(1920, 1280)
