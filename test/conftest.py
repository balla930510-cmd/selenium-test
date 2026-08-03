import os
from datetime import datetime

import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    # 只處理 test execution 階段
    if report.when != "call":
        return

    # 只有失敗才截圖
    if not report.failed:
        return

    driver = item.funcargs.get("driver")

    if driver is None:
        return

    # =========================
    # Screenshot directory
    # =========================

    screenshot_dir = os.path.join(
        os.getcwd(),
        "screenshots"
    )

    os.makedirs(
        screenshot_dir,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"{item.name}_{timestamp}.png"
    )

    filepath = os.path.join(
        screenshot_dir,
        filename
    )

    # =========================
    # Save screenshot
    # =========================

    success = driver.save_screenshot(filepath)

    print(f"\nScreenshot saved: {filepath}")
    print(f"Screenshot success: {success}")

    if not success:
        return

    # =========================
    # Attach screenshot to Allure
    # =========================

    with open(filepath, "rb") as image_file:
        allure.attach(
            image_file.read(),
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

    print("Failure Screenshot attached to Allure")