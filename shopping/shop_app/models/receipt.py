from django.db import models
from .customer import Customer
from .product import Product

class Receipt(models.Model):
  class Meta:
    db_table = 'receipts'

  total = models.DecimalField(max_digits = 8, decimal_places = 2, blank = False)
  product = models.ForeignKey(Product, on_delete = models.CASCADE, blank = False)
  product_count = models.SmallIntegerField(blank = False)
  customer = models.ForeignKey(Customer, on_delete = models.CASCADE, blank = False)
  confirmation_code = models.CharField(max_length = 100, blank = True)
