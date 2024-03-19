from django.db import models
from django.utils import timezone
from .models import User  # Import des User-Modells aus der gleichen Datei oder entsprechendem Paket

class Entry(models.Model):
    entry_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    journal = models.BooleanField(default=True)

    def __str__(self):
        return f"Entry {self.entry_id} by {self.user.email}"