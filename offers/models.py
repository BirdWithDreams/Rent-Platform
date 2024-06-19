import uuid

from django.db import models

from authentication.models import CustomUser




# Create your models here.
class Offers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    tags = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='offers-images/', blank=True)


class Contract(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='contract_seller')
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='contract_buyer')
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    buyer_first_name = models.CharField(max_length=30)
    buyer_last_name = models.CharField(max_length=30)
    buyer_email = models.EmailField()
    buyer_city = models.CharField(max_length=20)
    buyer_location = models.CharField(max_length=128)
