from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.
from django.urls import reverse

from Market.models import Product

def createUser(name):
    return User.objects.create_user(username=name, password="tester")

def createListing(name, user):
    return Product.objects.create(owner=user, product_name=name, description="test des", price=100, stock=5)



class ListingFunctionsTests(TestCase):
    """
        Test:
        - update listing: changed = true

    """



class CartFunctionsTests(TestCase):
    """
        Test:
        - add_to_cart:
        - remove from cart:
            - both done by testing quantity values

    """

    def test_add_to_cart(self):
        user = createUser("u1")
        createListing("l1", user)

