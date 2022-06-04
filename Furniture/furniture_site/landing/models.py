from django.db import models


class MainImage(models.Model):
    image_title = models.CharField(max_length=50, verbose_name="Название проекта")
    image = models.ImageField(upload_to='landing/', verbose_name="Фотография")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создана")
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Изменена")

    def __str__(self):
        return "%s" % self.pk

    class Meta:
        verbose_name = 'Фотография проектов'
        verbose_name_plural = 'Фотографии проектов'


class ContactForm(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="Имя")
    last_name = models.CharField(max_length=200, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=200, verbose_name="Номер телефона")
    email = models.EmailField(max_length=200, verbose_name="Почта")
    message = models.TextField(max_length=1000, verbose_name="Сообщение")

    def __str__(self):
        # Будет отображаться следующее поле в панели администрирования
        return self.email

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
