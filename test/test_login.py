from pages.login_page import LoginPage


def test_login_success(driver):
    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        "tomsmith",
        "SuperSecretPassword!"
    )

    assert "You logged into a secure area!" in driver.page_source