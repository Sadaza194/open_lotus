from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Journal(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"Journal {self.id} by {self.author}\n {self.text}"
