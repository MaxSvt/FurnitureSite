# Generated by Django 4.0.2 on 2022-03-12 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_productincart_nmb_productincart_count_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinorder',
            old_name='nmb',
            new_name='count',
        ),
    ]
