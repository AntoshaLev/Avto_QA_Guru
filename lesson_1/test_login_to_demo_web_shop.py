from selene.support.shared import browser
from selene import be, have


def test_successful_login():
    browser.open('https://demowebshop.tricentis.com/')
    browser.element('.ico-login').click()

    browser.element('#Email').type('www.Garu33@mail.ru')
    browser.element('#Password').type('qwerty123')
    browser.element('.login-button').click()

    browser.element('.header .account').should(have.text('www.Garu33@mail.ru'))
    browser.element('.ico-logout').should(be.visible)
