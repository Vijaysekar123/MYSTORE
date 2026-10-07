
import pytest
import allure

from pages.Homepage import Homepage


@allure.title("Verify product search")
@allure.description("Verify that the user can search for products using different search inputs")
@allure.severity(allure.severity_level.CRITICAL)
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

    with allure.step("Search for the product"):
        home.Search(search_item)

    with allure.step("Get the search results"):
        product_names = home.get_product_names()

    with allure.step("Verify search results are displayed"):
        assert len(product_names) > 0

    with allure.step("Verify search URL"):
        assert '/search/' in home.get_current_url()


@allure.title("Verify product details")
@allure.description("Verify product URL, product title, product image and product price")
@allure.severity(allure.severity_level.CRITICAL)
def test_product_details(logged_in):
    home = Homepage(logged_in)

    with allure.step("Search for bag"):
        home.Search("bag")

    with allure.step("Get the first product name"):
        product_names = home.get_product_names()
        result_title = product_names[0]

    with allure.step("Open the first product"):
        home.click_first_product()

    with allure.step("Verify product URL"):
        assert '/product/' in home.get_current_url()

    with allure.step("Verify product title"):
        detail_title = home.get_product_title()
        assert result_title == detail_title

    with allure.step("Verify product image is displayed"):
        assert home.is_product_image_displayed()

    with allure.step("Verify product price is displayed"):
        price = home.get_product_price()
        assert price != ''

