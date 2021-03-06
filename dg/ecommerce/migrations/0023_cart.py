# Generated by Django 3.0.6 on 2020-05-23 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0022_profile_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_ip', models.CharField(max_length=255, verbose_name='ipaddress')),
                ('C_qty', models.IntegerField(max_length=255, verbose_name='Quantity')),
                ('C_total', models.IntegerField(max_length=255, verbose_name='Quantity')),
                ('C_Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Product', verbose_name='prodct')),
                ('C_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Category', verbose_name='Category')),
            ],
        ),
    ]
