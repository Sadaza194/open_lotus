from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Memory(models.Model):
    emotion = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return f"{self.date} \n \t {self.emotion} \n \t {self.text}"