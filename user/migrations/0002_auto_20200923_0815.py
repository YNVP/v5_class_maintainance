# Generated by Django 3.1.1 on 2020-09-23 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='roll_no',
            field=models.CharField(default='121710313000', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='section',
            field=models.CharField(default='B00', max_length=4),
            preserve_default=False,
        ),
    ]
