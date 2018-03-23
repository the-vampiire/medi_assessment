from django.db import models
from .category import Category

class Product(models.Model):
  class Meta:
    db_table = 'products'

  name = models.CharField(max_length = 50, blank = False)
  description = models.TextField(blank = False)
  cost = models.DecimalField(max_digits = 6, decimal_places = 2, blank = False)
  inventory = models.PositiveIntegerField(default = 1)
  image_url = models.TextField(blank = False, null = True)
  category = models.ForeignKey(Category, on_delete = models.CASCADE, blank = False)

  def __str__(self):
    return '%s: %s' % (self.category.name, self.name)