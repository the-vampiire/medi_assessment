from django.forms import ModelForm
from shop_app.models import Customer

class CustomerForm(ModelForm):
  class Meta:
    model = Customer
    fields = ('first_name', 'last_name', 'email', 'phone')

  # override to inject bootstrap class
  # https://stackoverflow.com/a/31627454/7542831
  def __init__(self, *args, **kwargs):
    super(CustomerForm, self).__init__(*args, **kwargs)
    for field in iter(self.fields):
      self.fields[field].widget.attrs.update({ 'class': 'form-control' })