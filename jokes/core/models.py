from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=255, null=True)
    strongly_typed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Joke(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    text = models.TextField()
    how_funny = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class ToldJoke(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joke = models.ForeignKey(Joke, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
