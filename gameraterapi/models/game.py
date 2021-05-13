from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    num_of_players = models.IntegerField()
    game_time_length = models.IntegerField()
    age_recommendation = models.IntegerField()
    categories = models.ManyToManyField(
        "Category", through="GameCategory", related_name="games")
