# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20151126_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('directorName', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hero_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Heroine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('heroine_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('producerName', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('morning_show', models.CharField(max_length=150)),
                ('matney_show', models.CharField(max_length=150)),
                ('first_show', models.CharField(max_length=150)),
                ('second_show', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('theatre_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie',
            new_name='movie_name',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='Sensor_rating',
            new_name='sensor_rating',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(to='movie.Director'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='hero',
            field=models.ForeignKey(to='movie.Hero'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='heroine',
            field=models.ForeignKey(to='movie.Heroine'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='producer',
            field=models.ForeignKey(to='movie.Producer'),
        ),
        migrations.AddField(
            model_name='theatre',
            name='movie',
            field=models.ForeignKey(to='movie.Movie'),
        ),
        migrations.AddField(
            model_name='shows',
            name='theatre',
            field=models.ForeignKey(to='movie.Theatre'),
        ),
    ]
