from django.db import models

# Create your models here.
class Memory(models.Model):
    memoryID = models.CharField(max_length=100)
    entryID = models.CharField(max_length=100)
    emotion = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField()
    