from django.db import models

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=255)
    question_type = models.IntegerField()
    active = models.BooleanField(default=True)
    frequency = models.CharField(max_length=20, default='daily')

    def __str__(self):
        return self.question_text