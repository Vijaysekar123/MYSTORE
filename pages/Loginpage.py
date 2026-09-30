
from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.logger import logger


class LoginPage:
    Using_Email = "//a[text()='Login with email']"
    Email = '[type="email"]'
    Password = '[type="password"]'
    Login = 'login-btn'
    dashboard = "//div[contains(@class,'ms-th-account-holder')]"
    error_message = "//div[contains(@class,'text-bg-danger')]"
    email_error = "//div[contains(@class,'error')]"
    password_error = "//span[contains(@class,'error')]"
    logout='[class="ms-th-account-holder fw-semibold text-dark text-capitalize text-truncate"]'
    logout_button='[class="link-dark d-block lh-sm p-1"]'
    forgot_password = "//a[text()='Forgot password?']"

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        WebDriverWait(self.driver, 40).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.Using_Email))
        ).click()

        logger.info("Login started")

        sleep(2)

        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.Email))).send_keys(email)

        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.Password))).send_keys(password)

        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.ID, self.Login))).click()

        logger.info("Login button clicked")


    def is_login_successful(self):
        return WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, self.dashboard))).is_displayed()

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, self.error_message)
            )
        ).text

    def get_required_field_message(self):
        email_errors = self.driver.find_elements(By.XPATH, self.email_error)
        password_errors = self.driver.find_elements(By.XPATH, self.password_error)

        for error in email_errors + password_errors:
            if error.is_displayed():
                return error.text


    def Logout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.Logout).click()
        self.driver.find_element(By.XPATH, self.logout_button).click()

