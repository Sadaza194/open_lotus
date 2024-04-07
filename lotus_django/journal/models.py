from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Journal(models.Model):
    # id = models.AutoField(primary_key=True default=1)
    text = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.date} \n \t {self.text}"
