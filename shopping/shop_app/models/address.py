from django.db import models
from django.core.validators import RegexValidator

class Address(models.Model):
  class Meta:
    db_table = 'addresses'

  _zip_validator = RegexValidator(
    regex = r'^\d{5}$',
    message = 'Must enter a valid 5 digit zip code'
  )
  street = models.CharField(max_length = 255, blank = False)
  zipcode = models.CharField(max_length = 5, validators = [_zip_validator], blank = False)
  city = models.CharField(max_length = 30, blank = False)
  state = models.CharField(max_length = 13, blank = False)

  def __str__(self):
    return '%s, %s - %s, %s' % (self.street, self.zipcode, self.city, self.state)
  