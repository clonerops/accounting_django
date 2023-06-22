# Generated by Django 4.2.2 on 2023-06-22 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_productgroupid'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='order',
            name='isPayment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='productId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_detail', to='product.product', verbose_name='محصول'),
            preserve_default=False,
        ),
    ]