# Generated by Django 3.1.1 on 2020-11-04 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_request', '0005_auto_20201104_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancerequest',
            name='request_type',
            field=models.CharField(blank=True, choices=[('Training', 'Assessment'), ('A', 'Assessment')], max_length=20, null=True),
        ),
    ]
