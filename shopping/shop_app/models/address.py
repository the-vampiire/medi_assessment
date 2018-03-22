from django.db import models

class Address(models.Model):
  class Meta:
    db_table = 'addresses'

  street = models.CharField(max_length = 255, blank = False)
  zipcode = models.CharField(max_length = 5, blank = False)
  city = models.CharField(max_length = 30, blank = False)
  state = models.CharField(max_length = 13, blank = False)

  def __str__(self):
    return '%s, %s - %s, %s' % (self.street, self.zipcode, self.city, self.state)
  