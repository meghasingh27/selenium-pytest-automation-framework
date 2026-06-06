from pages.login_page import LoginPage


def test_valid_login(driver):

    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "inventory" in driver.current_url