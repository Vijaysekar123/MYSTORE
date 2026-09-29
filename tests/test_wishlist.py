from pages.WishListpage import WishList
from pages.Homepage import Homepage


def test_wishlist_page(setup):
    wishlist = WishList(setup)

    wishlist.wishlistpage()

    assert '/wishlist' in wishlist.driver.current_url


def test_add_to_wishlist(setup):
    home = Homepage(setup)
    wishlist = WishList(setup)

    home.Search("WATCH")
    home.click_first_product()

    wishlist.click_heart()

    assert wishlist.is_heart_pink()


def test_product_added_to_wishlist(setup):
    home = Homepage(setup)
    wishlist = WishList(setup)

    home.Search("Laptop")
    home.click_first_product()
    wishlist.click_heart()

    wishlist.wishlistpage()

    products = wishlist.get_wishlist_products()

    assert any("Laptop" in product for product in products)


def test_multiple_products_added_to_wishlist(setup):
    home = Homepage(setup)
    wishlist = WishList(setup)

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


def test_delete_product_from_wishlist(setup):
    wishlist = WishList(setup)

    wishlist.wishlistpage()

    products = wishlist.get_wishlist_products()
    print(products)

    wishlist.cancel()

    products = wishlist.get_wishlist_products()
    print(products)