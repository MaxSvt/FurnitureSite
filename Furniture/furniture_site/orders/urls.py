from django.urls import path
from .views import *

urlpatterns = [
    path(r'cart_adding/', cart_adding, name='cart_adding'),
    path(r'checkout/', checkout, name='checkout'),
]
