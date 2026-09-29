import pytest

# @pytest.fixture(scope='session',autouse=True)
@pytest.fixture
def setup():
    from selenium import webdriver
    from time import sleep
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.mystore.in/en/user/login?redirect=%2Fen%2F')
    driver.implicitly_wait(10)
    sleep(3)
    # from pages.Loginpage import LoginPage
    # from time import sleep
    # sleep(3)
    # login_page = LoginPage(driver)
    # login_page.login('vjj.rain@gmail.com','Vj@15104089')
    yield driver
    driver.quit()