import pytest

from pages.Loginpage import LoginPage
from time import sleep



@pytest.mark.smoke
def test_login(setup):
    l=LoginPage(setup)
    l.login('vjj.rain@gmail.com','Vj@15104089')
    assert l.is_login_successful()
    sleep(5)



@pytest.mark.parametrize(["email","password"], [
('vjj.rain@gmail.com', '12345'),('vjj@gmail.com','Vj@15104089'),('rain@gmail.com','987456')
])
def test_login_invalid_login(setup,email,password):
    # setup.get('https://www.mystore.in/en/user/login?redirect=%2Fen%2F')

    login = LoginPage(setup)

    login.login(email,password)

    error_message = login.get_error_message()

    assert error_message == "User id or password is wrong"



@pytest.mark.parametrize(["email","password"], [
('vjj.rain@gmail.com', ''),('','Vj@15104089'),('','')
])
def test_login_without_fields(setup, email, password):

    # setup.get('https://www.mystore.in/en/user/login?redirect=%2Fen%2F')

    login = LoginPage(setup)

    login.login(email, password)

    required_message = login.get_required_field_message()

    assert required_message == "Required Field"



