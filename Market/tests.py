from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.
from Market.models import Product


def createListing():
    user = User.objects.create_user(username="tester", password="tester")
    return Product.objects.create(owner=user, product_name="test", description="test des", price=100, )

class ListingFunctionsTests(TestCase):
    """
        Test:
        - creat_listing: returns an object when searched in Listings
        - update listing: changed = true
        - delete listing: returns does not exists when looked for in Listings
    """


class CartFunctionsTests(TestCase):
    """
        Test:
        - add_to_cart:
        - remove from cart:
            - both done by testing quantity values

    """
