from django.forms import ModelForm
from shop_app.models import Address

class AddressForm(ModelForm):
  class Meta:
    model = Address
    fields = ('street', 'zipcode', 'city', 'state')
    
  # override to inject bootstrap class
  # https://stackoverflow.com/a/31627454/7542831
  def __init__(self, *args, **kwargs):
    super(AddressForm, self).__init__(*args, **kwargs)
    for field in iter(self.fields):
      self.fields[field].widget.attrs.update({ 'class': 'form-control' })