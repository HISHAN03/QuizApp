from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    usn = models.CharField(max_length=20)

    # Add any additional fields or methods as needed

    def __str__(self):
        return self.email


class YourScoreModel(models.Model):
    username = models.CharField(max_length=255, unique=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.username