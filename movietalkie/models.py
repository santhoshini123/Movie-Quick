from django.db import models

# Create your models here.
class Test(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()

	def clean_name(self):
		if len(self.name) < 4:
			raise ValueError("More than 4 required")
		return self.name

	def __unicode__(self):
		return self.name