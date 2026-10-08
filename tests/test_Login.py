import os

import pytest
import allure

from pages.Loginpage import LoginPage


@allure.title("Verify successful login")
@allure.description("Verify that a valid user can successfully log in")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
def test_login(setup):
    login = LoginPage(setup)
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")



    with allure.step("Enter valid login credentials"):
        login.login(email, password)

    with allure.step("Verify successful login"):
        assert login.is_login_successful()


@allure.title("Verify login with invalid credentials")
@allure.description("Verify that login fails when invalid credentials are provided")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(["email", "password"], [
    ('vjj.rain@gmail.com', '12345'),
    ('vjj@gmail.com', 'Vj@15104089'),
    ('rain@gmail.com', '987456')
])
def test_login_invalid_login(setup, email, password):
    login = LoginPage(setup)

    with allure.step("Enter invalid login credentials"):
        login.login(email, password)

    with allure.step("Get login error message"):
        error_message = login.get_error_message()

    with allure.step("Verify invalid login error message"):
        assert error_message == "User id or password is wrong"


@allure.title("Verify login with blank credentials")
@allure.description("Verify that blank text fields show Required Field error message")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(["email", "password"], [
    ('vjj.rain@gmail.com', ''),
    ('', 'Vj@15104089'),
    ('', '')
])
def test_login_without_fields(setup, email, password):
    login = LoginPage(setup)

    with allure.step("Enter blank login credentials"):
        login.login(email, password)

    with allure.step("Get required field error message"):
        required_message = login.get_required_field_message()

    with allure.step("Verify Required Field error message"):
        assert required_message == "Required Field"

