from django.db import models


class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    game = models.ForeignKey("Game")
    player = models.OneToOneField("User")