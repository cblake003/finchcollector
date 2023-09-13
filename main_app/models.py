from django.db import models

# Create your models here.

class Finch(models.Model):
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
