from django.db import models


class Category(models.Model):
    game_type = models.CharField(max_length=50)
