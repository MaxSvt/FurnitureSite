from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from orders.models import Order
from .forms import *
from .utils import *


class FurnitureHome(DataMixin, ListView):
    template_name = 'furniture_app/all_products.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Мебель')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ProductCategory(DataMixin, ListView):
    template_name = 'furniture_app/all_products.html'
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


class RegisterUser(DataMixin, CreateView):
    form_class = ResisterUserForm
    template_name = 'furniture_app/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'furniture_app/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_success_url(self):
        return reverse_lazy('home')


class ShowProfilePageView(DataMixin, DetailView):
    model = User
    template_name = 'furniture_app/user_profile.html'
    context_object_name = 'user'

    def get_context_data(self, *args, **kwargs):
        users = User.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(User, id=self.kwargs['pk'])
        user_order = Order.objects.all()
        c_def = self.get_user_context(title="Профиль")
        context['page_user'] = page_user
        context['users'] = users
        context['user_order'] = user_order
        context = dict(list(context.items()) + list(c_def.items()))
        return context


def logout_user(request):
    logout(request)
    return redirect('login')

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
#     return render(request, 'furniture_app/all_products.html', context=context)


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
#     return render(request, 'furniture_app/all_products.html', context=context)


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
