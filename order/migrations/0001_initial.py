# Generated by Django 4.2.2 on 2023-06-20 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderDate', models.DateTimeField(verbose_name='تاریخ سفارش')),
                ('settlementDate', models.DateTimeField(verbose_name='تاریخ تسویه')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('amount', models.CharField(max_length=255, verbose_name='مبلغ کل')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateField(auto_now=True)),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_detail', to='customer.customer', verbose_name='سفارش دهنده')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
