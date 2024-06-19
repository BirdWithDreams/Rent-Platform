from django.db import models
from django.contrib.auth.models import AbstractUser

# TODO: Add balance field
# Create your models here.
class CustomUser(AbstractUser):
    card = models.IntegerField(null=True, blank=True, )
    city = models.CharField(max_length=20, null=True, blank=True, )
    location = models.CharField(max_length=128, null=True, blank=True)
