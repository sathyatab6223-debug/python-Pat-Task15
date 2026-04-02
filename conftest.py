import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_configure(config):
    """
    Configure pytest to generate HTML report.
    """
    config.option.htmlpath = "reports/login_test_report.html"
    config.option.self_contained_html = True


@pytest.fixture(scope="session")
def driver():
    """
    Setup: Initialize Chrome, maximize window.
    Explicit waits are used in BasePage - no implicit wait.
    """
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()