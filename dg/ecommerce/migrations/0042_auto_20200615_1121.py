# Generated by Django 3.0.6 on 2020-06-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0041_auto_20200614_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='C_isorder',
            field=models.BooleanField(),
        ),
    ]