from django.db import models

class help(models.Model):
    tille = models.CharField(max_length=200)
    body = models.TextField()
    