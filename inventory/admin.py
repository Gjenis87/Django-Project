from django.contrib import admin
from inventory.models import Product
from inventory.models import Company
from users.models import UserInventory

admin.site.register(Product)
admin.site.register(Company)
admin.site.register(UserInventory)
