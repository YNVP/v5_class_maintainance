# Generated by Django 3.1.1 on 2020-09-27 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20200927_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_cr',
            field=models.BooleanField(default=False),
        ),
    ]
