# Generated by Django 3.0.6 on 2020-06-12 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0031_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_ip', models.CharField(max_length=255, verbose_name='ipaddress')),
                ('C_qty', models.IntegerField(blank=True, max_length=255, null=True, verbose_name='Quantity')),
                ('C_total', models.IntegerField(blank=True, max_length=255, null=True, verbose_name='total')),
                ('C_Product', models.ManyToManyField(blank=True, null=True, to='ecommerce.Product', verbose_name='Product')),
                ('C_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Category', verbose_name='Category')),
            ],
        ),
    ]
