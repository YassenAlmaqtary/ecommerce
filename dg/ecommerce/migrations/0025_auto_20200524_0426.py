# Generated by Django 3.0.6 on 2020-05-24 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0024_auto_20200524_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='C_Product',
            field=models.IntegerField(verbose_name='prodct'),
        ),
    ]