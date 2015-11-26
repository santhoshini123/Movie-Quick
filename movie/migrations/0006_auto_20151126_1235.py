# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20151126_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default=0, max_length=150),
        ),
        migrations.AddField(
            model_name='movie',
            name='hero',
            field=models.CharField(default=0, max_length=150),
        ),
        migrations.AddField(
            model_name='movie',
            name='heroine',
            field=models.CharField(default=0, max_length=150),
        ),
        migrations.AddField(
            model_name='movie',
            name='producer',
            field=models.CharField(default=0, max_length=150),
        ),
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='no_of_shows',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='no_of_theatre',
        ),
    ]
