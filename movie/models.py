from django.db import models
class SignUp(models.Model):
	First_name = models.CharField(max_length = 120, blank = False, null = True)
	Last_name = models.CharField(max_length = 120, blank = False, null = True)
	Email = models.EmailField(unique = True)
	Password = models.CharField(max_length = 10, blank = False, null = True)
	Re_Enter_password = models.CharField(max_length = 10, blank = True, null = False)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
class Hero(models.Model):
	hero_name = models.CharField(max_length = 150)
	def __str__(self):
		return self.hero_name
class Heroine(models.Model):
	heroine_name = models.CharField(max_length = 150)
	def __str__(self):
		return self.heroine_name
class Producer(models.Model):
	producerName = models.CharField(max_length = 150)
	def __str__(self):
		return self.producerName
class Director(models.Model):
	directorName = models.CharField(max_length = 150)
	def __str__(self):
		return self.directorName
class Movie(models.Model):
	movie_name= models.CharField(max_length = 200)
	hero = models.ForeignKey('Hero')
	heroine = models.ForeignKey('Heroine')
	director = models.ForeignKey('Director')
	producer = models.ForeignKey('Producer')
	sensor_rating = models.FloatField(default = 0)
	def __str__(self):
		return self.movie_name

class Theatre(models.Model):
	theatre_name = models.CharField(max_length = 100)
	movie = models.ForeignKey('Movie')

class Shows(models.Model):
	theatre = models.ForeignKey('Theatre')
	morning_show = models.CharField(max_length = 150)
	matney_show = models.CharField(max_length = 150)
	first_show = models.CharField(max_length = 150)
	second_show = models.CharField(max_length = 150)


# class Reviews(models.Model):
# 	user_rating = models.CharField(max_length = 150)
# 	userName = models.Model(max_length = 150)
# 	movie = models.Model(max_length = 150)
# 	userReviews = models.Model(max_length = 500)


