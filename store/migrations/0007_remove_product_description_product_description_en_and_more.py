# Generated by Django 4.2.3 on 2023-09-05 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_category_name_category_name_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_fa',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 5, 14, 16, 0, 933351, tzinfo=datetime.timezone.utc), verbose_name='datetime_created'),
        ),
    ]
