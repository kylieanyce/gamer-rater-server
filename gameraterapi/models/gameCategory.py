from django.db.models.deletion import CASCADE
from django.db import models


class GameCategory(models.Model):
    category = models.ForeignKey("Category", on_delete=CASCADE)
    game = models.ForeignKey("Game", on_delete=CASCADE)
