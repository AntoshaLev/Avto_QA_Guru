from selene import browser, be, have


def test_search_one():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser ... - GitHub'))


def test_search_two():
    browser.element('[name="q"]').should(be.blank).type('weqweqwr qewr qwrqw qwrqwr qwqwr').press_enter()
    browser.element(' [id="result-stats"]').should(have.text('Результатов: примерно 0'))

