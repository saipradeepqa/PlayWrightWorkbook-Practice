from playwright.sync_api import Page
class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def goto(self):
        self.page.goto("https://www.saucedemo.com/v1/")

    def login(self,username,password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
