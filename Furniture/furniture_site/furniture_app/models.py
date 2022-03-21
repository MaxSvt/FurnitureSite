from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", null=True, default=None)
    short_description = models.TextField(verbose_name="Характеристики", blank=True, null=True, default=None)
    image = models.ImageField(verbose_name="Изображение")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = "Мебель"
        verbose_name_plural = "Мебель"
        ordering = ['id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('furniture', kwargs={'product_slug': self.slug})


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, verbose_name="Товар", on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='products_images/', verbose_name="Фотография")
    is_main = models.BooleanField(default=False, verbose_name="Основная")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создана")
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Изменена")

    def __str__(self):
        return "%s" % self.pk

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name="Покупатель", on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    address = models.CharField(max_length=100, verbose_name="Адрес")

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатель"

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)
