from django.urls import path
from .views import *

urlpatterns = [
    path('product/', FurnitureHome.as_view(), name='furniture'),
    path('login/', login, name='login'),
    path('cart/', product_cart, name='product_cart'),
    path('category/<slug:category_slug>/', ProductCategory.as_view(), name='category'),
    path('product/<slug:product_slug>', ShowProduct.as_view(), name='product'),
]
