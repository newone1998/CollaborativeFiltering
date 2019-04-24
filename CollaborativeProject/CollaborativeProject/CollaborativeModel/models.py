# -- coding: utf-8 --
from django.db import models


class Song(models.Model):
    song_id = models.CharField(max_length=32, primary_key=True)
    title = models.CharField(max_length=255)
    star = models.DecimalField(max_digits=5, decimal_places=2)
    singer = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    classification = models.CharField(max_length=255)


class User(models.Model):
    name = models.CharField(max_length=255)
    gender = models.BooleanField()
    age = models.IntegerField()
    birth = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
