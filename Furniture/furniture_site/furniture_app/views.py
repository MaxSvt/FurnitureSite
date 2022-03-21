from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from orders.models import Order
from .utils import *


def login(request):
    context = {
        'login_page': login_page,
    }
    return render(request, 'furniture_app/login.html', context=context)


def product_cart(request):
    cart = Order.objects.all()
    context = {
        'cart': cart,
        'login_page': login_page,
    }
    return render(request, 'furniture_app/cart.html', context=context)


class FurnitureHome(DataMixin, ListView):
    template_name = 'furniture_app/product.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Мебель')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ProductCategory(DataMixin, ListView):
    template_name = 'furniture_app/product.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['products'][0].category))
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ShowProduct(DataMixin, DetailView):
    template_name = 'furniture_app/furniture.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['product'])
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# def main_product(request):
#     products_images = ProductImage.objects.filter(is_active=True, is_main=True)
#     categories = Category.objects.all()
#     context = {
#         'menu': menu,
#         'title': 'Мебель',
#         'categories': categories,
#         'products_images': products_images,
#         'login_page': login_page,
#         'cart_page': cart_page
#         }
#     return render(request, 'furniture_app/product.html', context=context)


# def show_category(request, category_slug):
#     products = Product.objects.filter(slug=category_slug)
#     categories = Category.objects.all()
#     context = {
#         'menu': menu,
#         'title': 'Мебель',
#         'products': products,
#         'categories': categories,
#         'category_selected': category_slug,
#     }
#     return render(request, 'furniture_app/product.html', context=context)


# def show_product(request, product_slug):
#     product = get_object_or_404(ProductImage, slug=product_slug)
#
#     context = {
#         'menu': menu,
#         'product': product,
#         'title': product.title,
#         'category_selected': product.category_id,
#     }
#
#     return render(request, 'furniture_app/furniture.html', context=context)
