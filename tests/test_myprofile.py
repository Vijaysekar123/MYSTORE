import pytest

from pages.Homepage import Homepage
from pages.Myprofilepage import MyProfile
from time import sleep

def test_profile(setup):
    Home=Homepage(setup)
    Home.Menu()
    profile=MyProfile(setup)
    profile.MyProfile()
    assert profile.is_profilepage_displayed()
    profile.Change_Name('Vijay','Kumar')
    sleep(2)
    profile.Cancel()
    sleep(5)