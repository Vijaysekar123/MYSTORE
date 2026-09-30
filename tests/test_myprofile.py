import pytest

from pages.Homepage import Homepage
from pages.Myprofilepage import MyProfile
from time import sleep

def test_profile(logged_in):
    Home=Homepage(logged_in)
    Home.Menu()
    profile=MyProfile(logged_in)
    profile.MyProfile()
    assert profile.is_profilepage_displayed()
    profile.Change_Name('Vijay','Kumar')
    sleep(2)
    profile.Cancel()
    sleep(5)