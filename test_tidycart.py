import pytest

from tidycart.cart import Cart
from tidycart.discount import apply_discount


def test_cart_total():
    cart = Cart()
    cart.add("pen", 2.5, 4)
    cart.add("book", 10)
    assert cart.total() == 20.0


@pytest.mark.parametrize("price,qty", [(-1, 1), (1, 0)])
def test_cart_rejects_bad_input(price, qty):
    with pytest.raises(ValueError):
        Cart().add("x", price, qty)


def test_discount():
    assert apply_discount(200, 25) == 150.0


def test_discount_rejects_bad_percent():
    with pytest.raises(ValueError):
        apply_discount(100, 120)
