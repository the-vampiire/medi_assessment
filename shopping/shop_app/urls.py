from django.urls import path
from .views import index

app_name = 'shop_app'

urlpatterns = [
  path('', index, name = 'index')
]