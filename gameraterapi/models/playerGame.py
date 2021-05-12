from django.db import models


class PlayerGame(models.Model):
    player = models.ForeignKey("User", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
