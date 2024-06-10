from django.db import models


class Participants(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    info = models.TextField()

    def __str__(self):
        return self.name
