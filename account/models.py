import uuid

from django.db import models

from authentication.models import CustomUser


class Feedbacks(models.Model):
    class Scores(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TEN = 10

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='feedback_reviewer')
    target = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='feedback_target')
    comment = models.TextField()
    score = models.IntegerField(choices=Scores.choices)
    created_at = models.DateTimeField(auto_now_add=True)
