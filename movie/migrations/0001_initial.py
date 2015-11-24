# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie', models.CharField(max_length=200)),
                ('year', models.IntegerField(default=0)),
                ('no_of_shows', models.IntegerField(default=0)),
            ],
        ),
    ]
