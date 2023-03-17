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


class CreditCard(models.Model):
    card_holder = models.ForeignKey(User, on_delete=models.CASCADE)
    credit_card_number = models.CharField(max_length=16, null=False, blank=False)
    expiration_date = models.CharField(max_length=6, null=False, blank=False)
    cvv_code = models.CharField(max_length=4, null=False, blank=False)
    credit_card_limit = models.DecimalField(max_digits=10, decimal_places=2)
    bilance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

