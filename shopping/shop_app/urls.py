from django.urls import path
from .views import index, category, product, purchase

app_name = 'shop_app'

urlpatterns = [
  path('', index, name = 'index'),
  path('category/<int:category_id>', category, name = 'category'),
  path('products/<int:product_id>', product, name = 'product'),
  path('products/<int:product_id>/purchase', purchase, name = 'purchase')
]