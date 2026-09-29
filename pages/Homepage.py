from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from utils.logger import logger



class Homepage:
    Hamburger_Menu="(//*[name()='svg'])[1]"
    search_box="(//input)[1]"
    products = "//div[@class='product-thumb']//img"
    product_title = "//h1[@class='product-name m-0 h4 fw-semibold text-break']"
    product_image = "//img[contains(@class,'feature-image')]"
    product_price = "//span[contains(@class,'price-new')]"
    def __init__(self, driver):
        self.driver = driver
    def Menu(self):
        self.driver.find_element(By.XPATH, self.Hamburger_Menu).click()
        sleep(2)

    def Search(self,search_item):
        S=self.driver.find_element(By.XPATH, self.search_box)
        S.send_keys(search_item)
        ob=ActionChains(self.driver)
        ob.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        logger.info('item searched')
        sleep(2)

    def get_product_names(self):
            products = self.driver.find_elements(By.XPATH, self.products)
            return [product.get_attribute("title") for product in products]

    def get_current_url(self):
        return self.driver.current_url

    def clear_search(self):
        S = self.driver.find_element(By.XPATH, self.search_box)
        S.clear()

    def get_search_value(self):
        S = self.driver.find_element(By.XPATH, self.search_box)
        return S.get_attribute("value")

    def click_first_product(self):
        self.driver.find_elements(By.XPATH, self.products)[0].click()

    def get_product_title(self):
        return self.driver.find_element(By.XPATH, self.product_title).text

    def is_product_image_displayed(self):
        return self.driver.find_element(By.XPATH, self.product_image).is_displayed()

    def get_product_price(self):
        return self.driver.find_element(By.XPATH, self.product_price).text

    def go_back(self):
        self.driver.back()
        sleep(2)

