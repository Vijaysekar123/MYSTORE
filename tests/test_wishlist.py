
import allure

from pages.WishListpage import WishList
from pages.Homepage import Homepage


@allure.title("Verify wishlist page")
@allure.description("Verify that the user can open the wishlist page")
@allure.severity(allure.severity_level.CRITICAL)
def test_wishlist_page(logged_in):
    wishlist = WishList(logged_in)

    with allure.step("Open the wishlist page"):
        wishlist.wishlistpage()

    with allure.step("Verify wishlist page URL"):
        assert '/wishlist' in wishlist.driver.current_url


@allure.title("Verify adding product to wishlist")
@allure.description("Verify that the user can add a product to the wishlist")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_wishlist(logged_in):
    home = Homepage(logged_in)
    wishlist = WishList(logged_in)

    with allure.step("Search for WATCH"):
        home.Search("WATCH")

    with allure.step("Open the first product"):
        home.click_first_product()

    with allure.step("Add the product to wishlist"):
        wishlist.click_heart()


@allure.title("Verify product added to wishlist")
@allure.description("Verify that the selected product is displayed in the wishlist")
@allure.severity(allure.severity_level.CRITICAL)
def test_product_added_to_wishlist(logged_in):
    home = Homepage(logged_in)
    wishlist = WishList(logged_in)

    with allure.step("Search for Gift"):
        home.Search("Gift")

    with allure.step("Open the first product"):
        home.click_first_product()

    with allure.step("Add the product to wishlist"):
        wishlist.click_heart()

    with allure.step("Open the wishlist page"):
        wishlist.wishlistpage()

    with allure.step("Get wishlist products"):
        products = wishlist.get_wishlist_products()
        print("Wishlist products:", products)

    with allure.step("Verify Gift product is added to wishlist"):
        assert any("Gift" in product for product in products)


@allure.title("Verify multiple products added to wishlist")
@allure.description("Verify that multiple products can be added and displayed in the wishlist")
@allure.severity(allure.severity_level.CRITICAL)
def test_multiple_products_added_to_wishlist(logged_in):
    home = Homepage(logged_in)
    wishlist = WishList(logged_in)

    with allure.step("Search for Laptop"):
        home.Search("Laptop")

    with allure.step("Open the first Laptop product"):
        home.click_first_product()

    with allure.step("Add Laptop product to wishlist"):
        wishlist.click_heart()

    home.go_back()

    with allure.step("Search for Shoe"):
        home.Search("Shoe")

    with allure.step("Open the first Shoe product"):
        home.click_first_product()

    with allure.step("Add Shoe product to wishlist"):
        wishlist.click_heart()

    home.go_back()

    with allure.step("Open the wishlist page"):
        wishlist.wishlistpage()

    with allure.step("Get wishlist products"):
        products = wishlist.get_wishlist_products()
        print("Wishlist products:", products)

    with allure.step("Verify Laptop product is in wishlist"):
        assert any("Laptop" or "Macbook " in product for product in products)

    with allure.step("Verify Shoe product is in wishlist"):
        assert any("Shoe" in product for product in products)


@allure.title("Verify deleting product from wishlist")
@allure.description("Verify that the user can delete a product from the wishlist")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_product_from_wishlist(logged_in):
    wishlist = WishList(logged_in)

    with allure.step("Open the wishlist page"):
        wishlist.wishlistpage()

    with allure.step("Get wishlist products before deletion"):
        products_before = wishlist.get_wishlist_products()

    with allure.step("Delete the wishlist product"):
        wishlist.cancel()

    with allure.step("Get wishlist products after deletion"):
        products_after = wishlist.get_wishlist_products()

    with allure.step("Verify product is deleted from wishlist"):
        assert len(products_after) < len(products_before)

