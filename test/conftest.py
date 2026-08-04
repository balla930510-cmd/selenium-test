import os
from datetime import datetime

import allure
import pytest


@pytest.fixture
def driver():
    # 你的 WebDriver 建立方式
    from selenium import webdriver

    driver = webdriver.Chrome()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            screenshot_name = (
                f"{item.name}_{timestamp}.png"
            )

            screenshot_path = os.path.join(
                screenshot_dir,
                screenshot_name
            )

            success = driver.save_screenshot(screenshot_path)

            print(f"\nScreenshot saved: {screenshot_path}")
            print(f"Screenshot success: {success}")

            if success:
                with open(screenshot_path, "rb") as image_file:
                    allure.attach(
                        image_file.read(),
                        name="Failure Screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )