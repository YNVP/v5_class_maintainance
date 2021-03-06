# Generated by Django 3.1.1 on 2020-11-10 13:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=200)),
                ('team_instructor', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('image', models.ImageField(default='user.png', upload_to='team_pics')),
                ('slug', models.SlugField(max_length=200)),
                ('project_name', models.CharField(max_length=200)),
                ('project_field', models.CharField(max_length=200)),
                ('project_level', models.CharField(choices=[('Definition', 'Definition'), ('Initiation', 'Initiation'), ('Planning', 'Planning'), ('Execution', 'Execution'), ('Monitoring & Control', 'Monitoring & Control'), ('Closure', 'Closure')], max_length=100)),
                ('team_leader', models.CharField(max_length=200)),
                ('team_members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
