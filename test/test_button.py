from pages.button_page import ButtonPage


def test_button_click(driver):
    button_page = ButtonPage(driver)

    button_page.open()

    button_page.click_add_element()

    assert button_page.is_delete_button_displayed()