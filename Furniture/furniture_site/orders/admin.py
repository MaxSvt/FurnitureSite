from django.contrib import admin

from orders.models import *


class ProductInOrderInLine(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created', 'updated')
    list_display_links = ('id', 'name')
    search_fields = ('name', )


admin.site.register(Status, StatusAdmin)


class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInOrderInLine]
    list_display = ('id', 'customer_name', 'total_price', 'status', 'created')
    list_display_links = ('id', 'customer_name')
    search_fields = ('customer_name', )


admin.site.register(Order, OrderAdmin)


class ProductInCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'session_key', 'product', 'count', 'price_per_item', 'total_price', 'is_active', 'created')
    list_display_links = ('id', 'product')
    search_fields = ('product', )


admin.site.register(ProductInCart, ProductInCartAdmin)

