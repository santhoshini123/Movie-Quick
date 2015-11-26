# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20151126_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Sensor_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='no_of_theatre',
            field=models.IntegerField(default=0),
        ),
    ]
