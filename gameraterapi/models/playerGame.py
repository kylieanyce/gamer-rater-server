from django.db import models


class PlayerGame(models.Model):
    player = models.OneToOneField("User")
    game = models.ForeignObject("Game")
