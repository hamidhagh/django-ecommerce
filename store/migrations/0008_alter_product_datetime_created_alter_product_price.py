# Generated by Django 4.2.3 on 2023-09-07 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_product_description_product_description_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 7, 9, 41, 16, 657843, tzinfo=datetime.timezone.utc), verbose_name='datetime_created'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='price'),
        ),
    ]
