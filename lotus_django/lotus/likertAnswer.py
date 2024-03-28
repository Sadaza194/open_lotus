from django.db import models
from .answer import Answer

class LikertAnswer(models.Model):
    likert_id = models.AutoField(primary_key=True)
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return f"LikertAnswer {self.likert_id} for Answer {self.answer.answer_id}"
