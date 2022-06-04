from django.contrib import admin

from landing.models import *


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_title', 'is_active', 'created', 'updated')
    list_display_links = ('id', 'image_title')
    search_fields = ('image_title',)


admin.site.register(MainImage, ProductImageAdmin)


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'email', 'message')
    list_display_links = ('id', 'phone_number', 'email')
    search_fields = ('email', 'phone_number', )


admin.site.register(ContactForm, ContactFormAdmin)
