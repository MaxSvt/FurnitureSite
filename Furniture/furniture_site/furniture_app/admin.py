from django.contrib import admin
from .models import *


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'is_main', 'is_active', 'created', 'updated')
    list_display_links = ('id', 'product')
    search_fields = ('product',)


admin.site.register(ProductImage, ProductImageAdmin)


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInLine]
    list_display = ('id', 'title', 'category', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'category')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)

admin.site.register(Customer)
