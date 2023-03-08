from django.db import models
from django.contrib.auth.models import User


class PhoneNumber(models.Model):
    country_code = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UserInventory(models.Model):
    comment = models.CharField(max_length=200, null=True, blank=True)
    product = models.ForeignKey('inventory.Product', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

