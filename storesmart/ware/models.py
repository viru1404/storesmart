from django.db import models
from django.contrib.auth.models import User

class Userform(models.Model):
    user = models.OneToOneField(User)
    flag = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.user
    


