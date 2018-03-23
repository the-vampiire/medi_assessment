from django.shortcuts import render
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from .models import Category, Product, Customer, Receipt
from .forms import AddressForm, CustomerForm

def index(request):
  context = {
    "title": "All Products",
    "tab_categories": Category.objects.all(),
    "products": Product.objects.all().order_by('category_id'),
  }
  return render(request, 'shop_app/index.html', context)

def category(request, category_id):
  active_category = Category.objects.get(pk = category_id)
  context = {
    "title": "%s products" % active_category.name,
    "tab_categories": Category.objects.all(),
    "active_category": category_id,
    "products": active_category.product_set.all(),
  }
  return render(request, 'shop_app/category_list.html', context)

def product(request, product_id):
  product = Product.objects.get(pk = product_id)
  active_category = product.category
  context = {
    "title": "%s - %s" % (active_category.name, product.name),
    "tab_categories": Category.objects.all(),
    "active_category": active_category.pk,
    "product": product
  }
  return render(request, 'shop_app/product_details.html', context)

def purchase(request, product_id):
  product = Product.objects.get(pk = product_id)
  active_category = product.category
  customer_form = CustomerForm(request.POST or None)
  billing_form = AddressForm(request.POST or None, prefix = 'billing')
  shipping_form = AddressForm(request.POST or None, prefix = 'shipping')

  context = {
    "title": "Purchase",
    "tab_categories": Category.objects.all(),
    "active_category": active_category.pk,
    "product": product,
    "customer_form": customer_form,
    "billing_form": billing_form,
    "shipping_form": shipping_form
  }

# POST request (submit and process forms)
  if request.method == 'POST':
    quantity = int(request.POST.get('quantity')) # convert to int
    same_address = True if request.POST.get('same_address') == 'on' else False # checkboxes return "on" ...? lol

    if all(
      (customer_form.is_valid(), billing_form.is_valid(),
      shipping_form.is_valid(), quantity > 0)
    ):
      billing_address = billing_form.save()
      customer = Customer(
          **customer_form.cleaned_data,
          billing_address = billing_address,
          shipping_address = billing_address if same_address else shipping_form.save()
      )
      customer.save()

      try:
        receipt = Receipt(customer = customer, product = product, quantity = quantity).save()
        success_context = {
          "title": "Purchase Confirmation",
          "tab_categories": Category.objects.all(),
          "active_category": active_category.pk,
          "product": product,
          "receipt": receipt
        }
      # purchase completed successfully
        return render(request, 'shop_app/receipt.html', success_context)
      except ValidationError:
        # not sure how to pass the ValidationError that is emitted by the Receipt clean() override
        # recreating the error here. sorry for the hack
        customer_form.add_error(NON_FIELD_ERRORS, 'The quantity [%d] requested is not available. Only [%d] of %s are in stock.' % (quantity, product.inventory, product.name))

        return render(request, 'shop_app/purchase.html', context)

# if form is invalid
    return render(request, 'shop_app/purchase.html', context)
  
# GET request (display purchase view with forms)
  return render(request, 'shop_app/purchase.html', context)
    

  

