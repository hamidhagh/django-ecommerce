# Generated by Django 4.2.3 on 2023-07-20 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=2, upload_to='images/'),
            preserve_default=False,
        ),
    ]
