from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.WishListpage import WishList
from pages.Homepage import Homepage


def test_wishlist_page(logged_in):
    wishlist = WishList(logged_in)

    wishlist.wishlistpage()

    assert '/wishlist' in wishlist.driver.current_url


def test_add_to_wishlist(logged_in):
    home = Homepage(logged_in)
    wishlist = WishList(logged_in)

    home.Search("WATCH")
    home.click_first_product()

    wishlist.click_heart()




def test_product_added_to_wishlist(logged_in):
    home = Homepage(logged_in)
    wishlist = WishList(logged_in)

    home.Search("Laptop")
    home.click_first_product()
    wishlist.click_heart()

    wishlist.wishlistpage()

    products = wishlist.get_wishlist_products()

    assert any("Laptop" in product for product in products)


def test_multiple_products_added_to_wishlist(logged_in):
    home = Homepage(logged_in)
    wishlist = WishList(logged_in)

    home.Search("Laptop")
    home.click_first_product()
    wishlist.click_heart()
    home.go_back()

    home.Search("Shoe")
    home.click_first_product()
    wishlist.click_heart()
    home.go_back()

    wishlist.wishlistpage()

    products = wishlist.get_wishlist_products()

    assert any("Laptop" in product for product in products)
    assert any("Shoe" in product for product in products)


def test_delete_product_from_wishlist(logged_in):
    wishlist = WishList(logged_in)

    wishlist.wishlistpage()

    products_before = wishlist.get_wishlist_products()

    wishlist.cancel()

    products_after = wishlist.get_wishlist_products()

    assert len(products_after) < len(products_before)