from pages.form_page import FormPage


def test_form_success(driver):
    form_page = FormPage(driver)

    form_page.open()

    form_page.enter_username("測試帳號")
    form_page.enter_password("123456")

    assert form_page.get_username() == "測試帳號"
    assert form_page.get_password() == "123456"