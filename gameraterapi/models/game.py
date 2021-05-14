from django.db import models
from django.db.models.deletion import CASCADE


class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    num_of_players = models.IntegerField()
    game_time_length = models.CharField(max_length=50)
    age_recommendation = models.CharField(max_length=50)
    categories = models.ManyToManyField(
        "Category", through="GameCategory", related_name="games")