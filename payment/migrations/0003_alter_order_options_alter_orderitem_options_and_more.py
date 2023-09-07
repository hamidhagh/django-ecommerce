# Generated by Django 4.2.3 on 2023-09-03 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_category_options_alter_product_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0002_order_orderitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Order Item', 'verbose_name_plural': 'Order Items'},
        ),
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name': 'Shipping Address', 'verbose_name_plural': 'Shipping Address'},
        ),
        migrations.AlterField(
            model_name='order',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='amount_paid'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_ordered'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(max_length=300, verbose_name='full_name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.TextField(max_length=10000, verbose_name='shipping_address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.order', verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveBigIntegerField(default=1, verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='address1',
            field=models.CharField(max_length=300, verbose_name='address1'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='address2',
            field=models.CharField(max_length=300, verbose_name='address2'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='city',
            field=models.CharField(max_length=255, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='full_name',
            field=models.CharField(max_length=300, verbose_name='full_name'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='zipcode',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='zipcode'),
        ),
    ]
