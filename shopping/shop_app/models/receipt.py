from django.db import models, IntegrityError, transaction
from django.core.exceptions import ValidationError
from .customer import Customer
from .product import Product

class Receipt(models.Model):
  class Meta:
    db_table = 'receipts'

  customer = models.ForeignKey(Customer, on_delete = models.CASCADE, blank = False)
  product = models.ForeignKey(Product, on_delete = models.CASCADE, blank = False)
  quantity = models.PositiveIntegerField(blank = False)
  total = models.DecimalField(max_digits = 8, decimal_places = 2, blank = True, editable = False)
  confirmation_code = models.CharField(max_length = 100, blank = True, editable = False)

  # https://docs.djangoproject.com/en/2.0/topics/db/transactions/#controlling-transactions-explicitly
  # https://docs.djangoproject.com/en/2.0/ref/models/querysets/#select-for-update
  def clean(self):
    """
    override to ensure a locked transaction for decrementing product inventory

    guarantees concurrency of product inventory using atomic transactions and the row-locking method select_for_update() 
    """
    super(Receipt, self).clean_fields()

    if self.quantity == 0:
      raise ValidationError({ 'quantity': 'Must enter a purchase quantity greater than zero' })

    try:
      with transaction.atomic():
        # locking the product row for inventory update
        product = Product.objects.select_for_update().get(pk = self.product.pk)

        if product.inventory == 0:
          raise ValidationError({ 'quantity': 'This product is no longer available' })

        product.inventory -= self.quantity
        product.save()
    except (IntegrityError):
      raise ValidationError({ 'quantity': 'The quantity [%d] requested is not available. Only [%d] of %s remain' % (self.quantity, self.product.inventory, self.product.name) })

    self.total = self.product.cost * self.quantity
    self.confirmation_code = self._generate_confirmation()

      
  def _generate_confirmation(self):
    """
    returns a confirmation code of the format (spaces inserted for readability):

    [category first letter] P [product_id] Q [quantity] C [customer_id] 
    """
    return '%sP%dQ%dC%d' % (
      self.product.category.name[:1].upper(),
      self.product.pk,
      self.quantity,
      self.customer.pk
    ) 

  def __str__(self):
    return '%s - %s ($%0.2f)' % (self.customer.email, self.confirmation_code, self.total)
