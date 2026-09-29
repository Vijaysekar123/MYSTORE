from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.logger import logger


class MyProfile:
    myprofile = '(//a[@class="d-flex align-items-center w-100 linked-btn lh-sm small fw-semibold position-relative py-2 px-3 rounded-3"])[1]'
    profile_page='[class="account-desktop pt-4 desktop profile"]'
    edit='[class="btn btn-light btn-md d-inline-flex align-items-center"]'
    First_name="//input[@name='First Name']"
    Last_name='//input[@name="Last Name"]'
    submit="//button[text()='Submit']"
    cancel='[class="d-flex fw-semibold align-items-center text-danger"]'
    def __init__(self, driver):
        self.driver = driver
    def MyProfile(self):
        self.driver.find_element(By.XPATH, self.myprofile).click()
        sleep(2)
        logger.info("MyProfile page displayed")
    def Change_Name(self, newFirstName,newLastName):
        self.driver.find_element(By.CSS_SELECTOR, self.edit).click()
        sleep(2)
        ob=ActionChains(self.driver)

        FN=self.driver.find_element(By.XPATH, self.First_name)
        ob.double_click(FN).perform()
        sleep(2)
        FN.send_keys(newFirstName)
        LN=self.driver.find_element(By.XPATH, self.Last_name)
        ob.double_click(LN).perform()
        sleep(2)
        LN.send_keys(newLastName)
        sleep(2)
        ele=WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.submit)))
        ele.click()
        logger.info("Name updated successfully")
        sleep(5)
    def Cancel(self):
        self.driver.find_element(By.CSS_SELECTOR, self.edit).click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, self.cancel).click()
    def is_profilepage_displayed(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.profile_page).is_displayed()

