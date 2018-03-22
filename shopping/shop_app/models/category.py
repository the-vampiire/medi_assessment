from django.db import models

class Category(models.Model):
  class Meta:
    db_table = 'categories'
    verbose_name = 'category'
    verbose_name_plural = 'categories'

  name = models.CharField(max_length = 50, blank = False)

  def __str__(self):
    return self.name

  