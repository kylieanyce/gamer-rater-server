from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class Image(models.Model):
    image = models.ImageField()
    player = models.ForeignKey(User, on_delete=CASCADE)
    game = models.ForeignKey("Game", on_delete=CASCADE)
