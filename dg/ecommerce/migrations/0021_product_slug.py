# Generated by Django 3.0.6 on 2020-05-22 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0020_auto_20200521_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]