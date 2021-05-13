from django.db import models
from django.contrib.auth.models import User


class PlayerGame(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
