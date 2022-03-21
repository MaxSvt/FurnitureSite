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
