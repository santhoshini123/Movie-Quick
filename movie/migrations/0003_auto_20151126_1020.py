# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_signup'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together=set([('movie', 'year')]),
        ),
    ]
