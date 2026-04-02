from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
   
    def __init__(self, driver):
        """Initialize browser instance & global wait timeouts."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def wait_for_element(self, locator):

        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element not found: {locator}")

    def wait_for_element_visible(self, locator):
        """Wait for element to be visible."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element not visible: {locator}")

    def wait_for_element_clickable(self, locator):
        """
        Wait for element to be clickable.
        """
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise Exception(f"Element not clickable: {locator}")

    def click(self, locator):
        self.wait_for_element_clickable(locator).click()

    def send_keys(self, locator, value):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        
        return self.wait_for_element_visible(locator).text

    def is_element_displayed(self, locator):
        try:
            return self.wait_for_element_visible(locator).is_displayed()
        except Exception:
            return False