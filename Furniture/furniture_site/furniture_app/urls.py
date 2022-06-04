from django.urls import path

from .views import *

urlpatterns = [
    path('product/', FurnitureHome.as_view(), name='furniture'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('account/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('category/<slug:category_slug>/', ProductCategory.as_view(), name='category'),
    path('product/<slug:product_slug>', ShowProduct.as_view(), name='product'),
    path('edit_profile/', edit, name='edit_profile'),
]
