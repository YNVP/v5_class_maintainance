# Generated by Django 3.1.1 on 2020-11-10 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20201110_2320'),
        ('meeting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='team',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='teams.team'),
        ),
    ]
