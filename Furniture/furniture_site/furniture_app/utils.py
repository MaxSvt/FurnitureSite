from django.shortcuts import render

from .models import *

menu = [
    {'title': "Главная", 'page_url': 'home'},
    {'title': "Мебель", 'page_url': 'furniture'},
    {'title': "О нас", 'page_url': 'about'},
    {'title': "Контакты", 'page_url': 'contact'},
]

login_page = [
    {'title': "Войти", 'page_url': 'login'},
]

cart_page = [
    {'title': "Корзина", 'page_url': 'product_cart'},
]


class DataMixin:
    model = Product

    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Category.objects.all()
        products_images = ProductImage.objects.filter(is_active=True, is_main=True)
        context['menu'] = menu
        context['login_page'] = login_page
        context['cart_page'] = cart_page
        context['categories'] = categories
        context['products_images'] = products_images
        return context
