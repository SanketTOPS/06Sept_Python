# Generated by Django 4.1.4 on 2022-12-29 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usersignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 29, 14, 13, 15, 629333))),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('username', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('mobile', models.BigIntegerField()),
            ],
        ),
    ]
