from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


def get_upload_path(instance, filename):
    return 'user-' + str(instance.owner.id) + '/' + filename


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    # product_picture = models.ImageField(upload_to=get_upload_path)
    description = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()
    pub_date = models.DateTimeField('date published', default=timezone.now)
    changed = models.BooleanField(default=False)

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=50, default="Name Missing")
    # product_picture = models.ImageField(upload_to=get_upload_path)
    description = models.CharField(max_length=50, default="No Description")
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)

class Listing(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

class Cart(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Address(models.Model):
    user = models.CharField(max_length=100, default=' ')
    line_one = models.CharField(max_length=100, default=' ')
    line_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, default='Montreal')
    province = models.CharField(max_length=30, default='QC')
    Country = models.CharField(max_length=30, default='Canada', blank=True)
    Zipcode = models.CharField(max_length=10, default='H1H 1H1')


