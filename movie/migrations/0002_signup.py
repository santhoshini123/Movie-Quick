# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('First_name', models.CharField(max_length=120, null=True)),
                ('Last_name', models.CharField(max_length=120, null=True)),
                ('Email', models.EmailField(unique=True, max_length=254)),
                ('Password', models.CharField(max_length=10, null=True)),
                ('Re_Enter_password', models.CharField(max_length=10, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
