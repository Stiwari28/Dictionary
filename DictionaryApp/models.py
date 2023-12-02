from django.db import models

# Create your models here.
# models.py

class Word(models.Model):
    word = models.CharField(max_length=100, unique=True)
    meaning = models.TextField()
    example = models.TextField()
    synonym = models.CharField(max_length=100)
    antonym = models.CharField(max_length=100)

    def __str__(self):
        return self.word

