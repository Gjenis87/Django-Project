from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    barcode = models.CharField(max_length=10, null=False, blank=False)
    expiry_date = models.DateTimeField(blank=False, null=False)
    quantity = models.IntegerField(blank=False , null=False)
    tag = models.CharField(max_length=10, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)


