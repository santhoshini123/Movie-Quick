# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20151126_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Sensor_rating',
            field=models.FloatField(default=0),
        ),
    ]
