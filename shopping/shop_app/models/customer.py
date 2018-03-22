from django.db import models
from .address import Address
from django.core.validators import RegexValidator

class Customer(models.Model):
  class Meta:
    db_table = 'customers'


  _phone_validator = RegexValidator(
    regex = r'^\d{10}$',
    message = 'Enter a valid 10 digit phone number starting with the area code'
  )
  first_name = models.CharField(max_length = 30, blank = False)
  last_name = models.CharField(max_length = 30, blank = False)
  email = models.EmailField(blank = False)
  phone = models.CharField(max_length = 10, validators = [_phone_validator], blank = False)
  billing_address = models.ForeignKey(Address, related_name = 'billing_addresses', on_delete = models.CASCADE, blank = False)
  shipping_address = models.ForeignKey(Address, related_name = 'shipping_addresses', on_delete = models.CASCADE, blank = True)

  def __str__(self):
    return self.email

