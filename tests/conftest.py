import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.mystore.in/en/user/login?redirect=%2Fen%2F")
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


@pytest.fixture
def logged_in(setup):
    from pages.Loginpage import LoginPage

    login_page = LoginPage(setup)

    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    login_page.login(email, password)

    return setup