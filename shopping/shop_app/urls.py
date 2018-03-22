from django.urls import path
from .views import index, category

app_name = 'shop_app'

urlpatterns = [
  path('', index, name = 'index'),
  path('category/<int:category_id>', category, name = 'category')
]