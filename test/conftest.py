import os
from datetime import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver():
    options = Options()

    # GitHub Actions / CI environment
    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")

    options.add_argument("--window-size=1920,1080")

    return webdriver.Chrome(options=options)


@pytest.fixture
def driver():
    driver = create_driver()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, driver):
    yield

    if request.node.rep_call.failed:

        os.makedirs("screenshots", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        screenshot_name = (
            f"{request.node.name}_{timestamp}.png"
        )

        screenshot_path = os.path.join(
            "screenshots",
            screenshot_name
        )

        driver.save_screenshot(screenshot_path)

        allure.attach.file(
            screenshot_path,
            name=screenshot_name,
            attachment_type=allure.attachment_type.PNG
        )