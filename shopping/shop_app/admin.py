from django.contrib import admin
from .models import Category, Product, Customer, Address, Receipt

admin.site.register([Category, Product, Customer, Address, Receipt])
