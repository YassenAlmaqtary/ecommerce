# Generated by Django 3.0.6 on 2020-05-20 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0015_remove_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Porduct/'),
        ),
    ]
