from django.contrib import admin
from users.models import PhoneNumber, CreditCard

admin.site.register(PhoneNumber)
admin.site.register(CreditCard)
