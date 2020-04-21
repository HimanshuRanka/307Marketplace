from django.contrib.auth.models import User
from django.db import models


# Create your models here.


def get_upload_path(instance, filename):
    return 'user-' + str(instance.owner.id) + '/' + filename


class Product(models.Model):
    # Not sure about the user attribute as
    # I havent looked into models as much so am not sure about the relationshi
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length = 50)
    product_picture = models.ImageField(upload_to=get_upload_path)
    description = models.CharField(max_length = 50)
    price = models.IntegerField()
    stock = models.IntegerField()


class User(models.Model):
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	username = models.CharField(max_length = 40)
	password = models.CharField(max_length = 40)
	email = models.CharField(max_length = 40)

class Purchase(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Address(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	address = models.CharField(max_length = 100)
