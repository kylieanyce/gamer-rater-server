from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
