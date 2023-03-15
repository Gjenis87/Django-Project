from django.urls import path
from inventory import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/create', views.create_product, name='create_product'),
    path('product/list', views.product_list, name='products'),
    path('product/<int:pk>', views.single_product, name='single_product'),
    path('product/edit/<int:pk>', views.edit_product, name="edit_product"),
    path('product/delete/<int:pk>', views.delete_product, name="delete_product"),
    path('product/company', views.create_company, name="create_company"),
    path('product/company/inventory', views.company_inventory, name="company_inventory"),
    path('product/company/sidebar', views.company_sidebar, name="company_sidebar"),

]
