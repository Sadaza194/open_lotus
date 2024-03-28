from django.db import models
from .entry import Entry 

class Memory(models.Model):
    memory_id = models.AutoField(primary_key=True)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=40)
    text = models.CharField(max_length=60)

    def __str__(self):
        return f"Memory {self.memory_id} for Entry {self.entry.entry_id}"

class Journal(models.Model):
    journal_id = models.AutoField(primary_key=True)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Journal {self.journal_id} for Entry {self.entry.entry_id}"