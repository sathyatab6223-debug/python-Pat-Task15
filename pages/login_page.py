from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils import config


class LoginPage(BasePage):
    """
    Page Object for the Login Page.
    Contains locators and actions related to user authentication.
    """

    # Locators
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    DASHBOARD_HEADER = (By.XPATH, "//h6[contains(@class, 'oxd-text') and text()='Dashboard']")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='oxd-alert-content']//p")
    USER_DROPDOWN = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(text(), 'Logout')]")

    def open(self, url):
        """Navigate to the Login Page URL."""
        self.driver.get(url)
        self.driver.maximize_window()

    def login(self, username, password):
        """
        Executes the full login flow with valid credentials.
        """
        # Wait for presence of username field (ensure we're on login page)
        self.wait.until(EC.presence_of_element_located(self.USERNAME_FIELD))
        self.send_keys(self.USERNAME_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def navigate_to_login_page(self):
        """Navigate back to login page and wait for elements."""
        self.driver.get(config.BASE_URL)
        # Wait for username field to be present
        self.wait.until(EC.presence_of_element_located(self.USERNAME_FIELD))

    def verify_dashboard_displayed(self):
        """Verify that dashboard is displayed after successful login."""
        return self.is_element_displayed(self.DASHBOARD_HEADER)

    def get_error_message(self):
        """Get error message for invalid login."""
        return self.get_text(self.ERROR_MESSAGE)

    def verify_invalid_login(self, username, password):
        """Verify that invalid credentials show error message."""
        self.wait.until(EC.presence_of_element_located(self.USERNAME_FIELD))
        self.send_keys(self.USERNAME_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
        return self.get_error_message()

    def logout(self):
        """Logout from the application."""
        # Click on user dropdown
        self.click(self.USER_DROPDOWN)
        # Click on logout
        self.click(self.LOGOUT_BUTTON)