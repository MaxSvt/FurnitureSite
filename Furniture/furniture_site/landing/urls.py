from django.urls import path
from landing.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
