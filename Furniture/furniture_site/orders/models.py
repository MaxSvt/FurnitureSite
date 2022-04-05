from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from utils.main import disable_for_loaddata

from furniture_app.models import *

User = get_user_model()


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None, verbose_name="Статус заказа")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Изменен")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None, verbose_name="Пользователь", on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Общая цена") #total price for all products in order
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name="Имя пользователя")
    customer_lastname = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name="Фамилия пользователя")
    customer_email = models.EmailField(blank=True, null=True, default=None, verbose_name="Почта")
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None, verbose_name="Номер телефона")
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None, verbose_name="Адрес")
    comments = models.TextField(blank=True, null=True, default=None, verbose_name="Пожелание")
    status = models.ForeignKey(Status, verbose_name="Статус", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Изменен")

    def __str__(self):
        return "Заказ %s %s" % (self.pk, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):

        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, verbose_name="Заказ", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, verbose_name="Продукт", on_delete=models.CASCADE)
    count = models.IntegerField(default=1, verbose_name="Количество")
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Цена за единицу")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Общая цена")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Изменен")

    def __str__(self):
        return "%s" % self.product.title

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        print(self.count)

        self.total_price = int(self.count) * price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


@disable_for_loaddata
def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)


class ProductInCart(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None, verbose_name="Заказ", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, verbose_name="Продукт", on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1, verbose_name="Количество")
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Цена за единицу")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Общая цена")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Изменен")

    def __str__(self):
        return "%s" % self.product.title

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = int(self.count) * price_per_item

        super(ProductInCart, self).save(*args, **kwargs)
