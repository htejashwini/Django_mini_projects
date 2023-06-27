from django.db import models

class Features(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
