from django.db import models
from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    barcode = models.CharField(max_length=10, null=False, blank=False)
    expiry_date = models.DateTimeField(blank=True, null=True)
    quantity = models.IntegerField(blank=False, null=False)
    tag = models.CharField(max_length=10, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    companies = models.ManyToManyField(User, through='Company')


class Company(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=60, null=False, blank=False)

