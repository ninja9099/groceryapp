from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    PROFILE_IMAGES = "images/profile/"
    avatar = models.ImageField(upload_to=PROFILE_IMAGES, blank=True)
