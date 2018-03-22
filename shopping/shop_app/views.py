from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product

def index(request):
  context = {
    "title": "All Products",
    "tab_categories": Category.objects.all()
  }
  return render(request, 'base.html', context)

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
