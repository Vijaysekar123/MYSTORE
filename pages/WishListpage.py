from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.Homepage import Homepage
from utils.logger import logger


class WishList:
    wishlist_button = '(//i[@class="bi bi-heart fs-5 lh-1 me-2"])[1]'
    cancel_button = '(//i[@class="bi bi-trash3-fill text-danger lh-1 fs-5"])[1]'
    heart_icon = "//i[contains(@class,'bi-heart') and contains(@class,'text-dark')]"
    pink_heart = "//i[contains(@class,'bi-heart-fill') and contains(@class,'pinkCol')]"
    wishlist_products = "//div[@class='product-thumb']//img"

    def __init__(self, driver):
        self.driver = driver

    def wishlistpage(self):
        Home = Homepage(self.driver)
        Home.Menu()
        self.driver.find_element(By.XPATH, self.wishlist_button).click()
        logger.info("Wishlist button clicked")
        sleep(2)

    def click_heart(self):
        heart = WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.heart_icon)
            )
        )
        heart.click()

    def is_heart_pink(self):
        return self.driver.find_element(By.XPATH, self.pink_heart).is_displayed()

    def get_wishlist_products(self):
        products = self.driver.find_elements(By.XPATH, self.wishlist_products)
        return [product.get_attribute("title") for product in products]

    def cancel(self):
        cancel_element = WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.cancel_button)
            )
        )
        cancel_element.click()
        logger.info("Cancel button clicked")