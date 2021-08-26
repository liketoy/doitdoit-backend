from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):

    avatar = models.ImageField()
    login_type = models.CharField(max_length=100)
    friends = models.ManyToManyField("self")
    badges = models.ManyToManyField("self")
