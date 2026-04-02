from pages.login_page import LoginPage
from utils import config
from utils.excel_utils import ExcelUtils


def test_login_data_driven(driver):
    """
    DATA DRIVEN TESTING: Read credentials from Excel and perform login tests.
    Writes test results (Pass/Fail), date, time back to Excel.
    """
    print(f"\nCurrent URL before open: {driver.current_url}")

    login = LoginPage(driver)
    login.open(config.BASE_URL)

    print(f"Current URL after open: {driver.current_url}")

    excel_utils = ExcelUtils(config.TEST_DATA_FILE)
    test_data = excel_utils.get_test_data()

    row_num = 2  # Start from row 2 (after header)

    for idx, test_case in enumerate(test_data, 1):
        username = test_case.get("Username")
        password = test_case.get("Password")

        print(f"\nTest {idx}: Username='{username}', Password='{password}'")
        print(f"Current URL: {driver.current_url}")

        # Perform login
        login.login(username, password)

        print(f"After login URL: {driver.current_url}")

        # Check if login was successful
        if login.verify_dashboard_displayed():
            test_result = "Pass"
            print("Result: PASS")
            # Logout to return to login page for next test
            login.logout()
        else:
            test_result = "Fail"
            print("Result: FAIL")

        # Write result, date, time to Excel
        excel_utils.write_result(row_num, test_result)
        row_num += 1

    # Save results and close
    excel_utils.save_results()
    excel_utils.close()