# Create your models here.
from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.word)
