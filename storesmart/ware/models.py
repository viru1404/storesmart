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
	cold_rate=models.PositiveSmallIntegerField(default=0 ,null=True)
	hot_rate=models.PositiveSmallIntegerField(default=0 ,null=True)
	mild_rate=models.PositiveSmallIntegerField(default=0 ,null=True)
	severe_rate=models.PositiveSmallIntegerField(default=0 ,null=True)
	cold_total=models.PositiveSmallIntegerField(default=0 ,null=True)
	hot_total=models.PositiveSmallIntegerField(default=0 ,null=True)
	mild_total=models.PositiveSmallIntegerField(default=0 ,null=True)
	severe_total=models.PositiveSmallIntegerField(default=0 ,null=True)
	cold_available=models.PositiveSmallIntegerField(default=0 ,null=True)
	hot_available=models.PositiveSmallIntegerField(default=0 ,null=True)
	mild_available=models.PositiveSmallIntegerField(default=0 ,null=True)
	severe_available=models.PositiveSmallIntegerField(default=0 ,null=True)

	def __str__(self):
		return self.location
    


