from django.db import models

# Create your models here.

from django.contrib.auth.models import User
# Create your models here.


class Label(models.Model):

    name = models.CharField(max_length=150)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):

        return self.name

