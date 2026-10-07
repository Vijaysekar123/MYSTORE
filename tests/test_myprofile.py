
import allure

from pages.Homepage import Homepage
from pages.Myprofilepage import MyProfile
from time import sleep


@allure.title("Verify profile page and change name")
@allure.description("Verify that the user can open the profile page and change the profile name")
@allure.severity(allure.severity_level.NORMAL)
def test_profile(logged_in):
    Home = Homepage(logged_in)

    with allure.step("Open the menu"):
        Home.Menu()

    profile = MyProfile(logged_in)

    with allure.step("Open the profile page"):
        profile.MyProfile()

    with allure.step("Verify profile page is displayed"):
        assert profile.is_profilepage_displayed()

    with allure.step("Change the profile name"):
        profile.Change_Name('Vijay', 'Kumar')

    sleep(2)

    with allure.step("Cancel the profile changes"):
        profile.Cancel()

    sleep(5)

