from django.db import models
from model_utils.models import TimeStampedModel


class SearchTopic(models.Model):
    name = models.CharField(max_length=255, unique=True)
    likes = models.IntegerField(default=0)
    num_of_search = models.IntegerField(default=0)

    def __str__(self):
        return self.name

