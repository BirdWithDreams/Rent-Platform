from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    card = models.IntegerField(null=True, blank=True, )
    city = models.CharField(max_length=20, null=True, blank=True, )
    location = models.CharField(max_length=128, null=True, blank=True)


class Wallet(models.Model):
    user_id = models.ForeignKey(CustomUser, primary_key=True, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
