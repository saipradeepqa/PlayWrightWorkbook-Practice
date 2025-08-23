import pytest

from pages.login_page import LoginPage

@pytest.fixture
def page(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

@pytest.fixture
def login_page(page):
    return LoginPage(page)


