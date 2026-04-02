# Configuration for the login automation framework

import os

# URLs
BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# Test data file path
TEST_DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "test_data.xlsx")