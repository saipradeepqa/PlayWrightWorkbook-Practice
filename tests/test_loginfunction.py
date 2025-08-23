import time

def test_successful_login(login_page):
    login_page.goto()
    login_page.login("standard_user","secret_sauce")
    time.sleep(5)
