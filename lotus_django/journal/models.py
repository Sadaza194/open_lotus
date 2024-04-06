from django.db import models
from django.utils import timezone
from lotus.models import User 

class Entry(models.Model):
    entry_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    is_journal = models.BooleanField(default=True)

    def __str__(self):
        return f"Entry {self.entry_id} by {self.user.email}"

class Journal(models.Model):
    journal_id = models.AutoField(primary_key=True)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Journal {self.journal_id} for Entry {self.entry.entry_id}"