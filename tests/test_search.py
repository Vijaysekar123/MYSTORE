from time import sleep

import pytest
from pages.Homepage import Homepage


@pytest.mark.parametrize("search_item", [
    "bag",
    "shoe",
    "hand bag",
    "HaNd BaG",
    " bag ",
    "12345",
    "@#$%"
])
def test_search(logged_in, search_item):
    home = Homepage(logged_in)

    home.Search(search_item)

    product_names = home.get_product_names()

    assert len(product_names) > 0
    assert '/search/' in home.get_current_url()            #to confirm its searching

def test_product_details(logged_in):
    home = Homepage(logged_in)

    home.Search("bag")

    product_names = home.get_product_names()
    result_title = product_names[0]

    home.click_first_product()

    assert '/product/' in home.get_current_url()

    detail_title = home.get_product_title()
    assert result_title == detail_title

    assert home.is_product_image_displayed()

    price = home.get_product_price()
    assert price != ''