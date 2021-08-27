from django.contrib.auth.models import AbstractUser
from django.db import models
from core import managers as core_managers


class User(AbstractUser):

    """Custom User Model"""

    LOGIN_GOOGLE = "google"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_GOOGLE, "Google"),
        (LOGIN_KAKAO, "Kakao"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    bio = models.TextField("bio", blank=True)
    login_method = models.CharField(max_length=50, choices=LOGIN_CHOICES)
    objects = core_managers.CustomUserManager()
