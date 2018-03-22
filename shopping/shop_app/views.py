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
