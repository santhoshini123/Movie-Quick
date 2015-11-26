from django.db import models
class SignUp(models.Model):
	First_name = models.CharField(max_length = 120, blank = False, null = True)
	Last_name = models.CharField(max_length = 120, blank = False, null = True)
	Email = models.EmailField(unique = True)
	Password = models.CharField(max_length = 10, blank = False, null = True)
	Re_Enter_password = models.CharField(max_length = 10, blank = True, null = False)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)

class Movie(models.Model):
	movie = models.CharField(max_length = 200)
	year = models.IntegerField(default = 0)
	hero = models.CharField(max_length = 150,default = 0)
	heroine = models.CharField(max_length = 150,default = 0)
	director = models.CharField(max_length = 150,default = 0)
	producer = models.CharField(max_length = 150,default = 0)
	Sensor_rating = models.FloatField(default = 0)

	
	


