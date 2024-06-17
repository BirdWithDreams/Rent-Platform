from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    card = models.IntegerField(default=None, null=True)
    city = models.CharField(max_length=20, default=None, null=True)
    location = models.CharField(max_length=128, default=None, null=True)

