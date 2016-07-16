from django.db import models
from django.contrib.auth.models import User

class Userform(models.Model):
    user = models.OneToOneField(User)
    flag = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.user.username


class warehouse(models.Model):
	user=models.CharField(max_length=200)
	location = models.CharField(max_length=1000)
	cold_total=models.PositiveSmallIntegerField(default=0)
	hot_total=models.PositiveSmallIntegerField(default=0)
	mild_total=models.PositiveSmallIntegerField(default=0)
	severe_total=models.PositiveSmallIntegerField(default=0)
	cold_available=models.PositiveSmallIntegerField(default=0)
	hot_available=models.PositiveSmallIntegerField(default=0)
	mild_available=models.PositiveSmallIntegerField(default=0)
	severe_available=models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return self.location

    


