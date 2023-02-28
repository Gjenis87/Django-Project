from django.db import models
from django.contrib.auth.models import User


class PhoneNumber(models.Model):
    country_code = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
