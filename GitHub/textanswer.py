from django.db import models
from .answer import Answer

class TextAnswer(models.Model):
    text_id = models.AutoField(primary_key=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    text = models.CharField(max_length=30)

    def __str__(self):
        return f"TextAnswer {self.text_id} for Answer {self.answer.answer_id}"