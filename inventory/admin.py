from django.contrib import admin
from inventory.models import Product
from inventory.models import Company

# Register your models here.

admin.site.register(Product)
admin.site.register(Company)

