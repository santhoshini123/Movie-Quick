from django.db import models

class Movie(models.Model):
	movie = models.CharField(max_length = 200)
	year = models.IntegerField(default = 0)
	no_of_shows = models.IntegerField(default = 0)