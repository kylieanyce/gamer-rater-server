from django.db import models


class Image(models.Model):
    image = models.ImageField()
    player = models.ForeignKey("Player")
    game = models.ForeignKey("Game")
