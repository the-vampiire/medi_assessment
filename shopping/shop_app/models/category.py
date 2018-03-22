from django.db import models

class Category(models.Model):
  class Meta:
    db_table = 'categories'
  name = models.CharField(max_length = 50, blank = False)
  