import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os
import allure

load_dotenv()


@pytest.fixture
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.mystore.in/en/user/login?redirect=%2Fen%2F")
    driver.implicitly_wait(10)

    yield driver

    if request.node.rep_call.failed:
        screenshot = driver.get_screenshot_as_png()

        allure.attach(
            screenshot,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)


@pytest.fixture
def logged_in(setup):
    from pages.Loginpage import LoginPage
    from pages.Homepage import Homepage

    login_page = LoginPage(setup)
    home = Homepage(setup)

    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    login_page.login(email, password)

    assert home.is_logged_in()

    return setup