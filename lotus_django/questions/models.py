from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    text = models.TextField(max_length=255, null=False)
    type = models.IntegerField(null=False)
    active = models.BooleanField(default=True, null=False)
    frequency = models.CharField(max_length=20, null=False, default="daily")

class QuestionTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"QuestionTracker for User {self.user.user_id} and Question {self.question.question_id}"
    
class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer {self.answer_id} by {self.user.email} for Question {self.question.question_id}"
    
class LikertAnswer(models.Model):
    likert_id = models.AutoField(primary_key=True)
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return f"LikertAnswer {self.likert_id} for Answer {self.answer.answer_id}"

class TextAnswer(models.Model):
    text_id = models.AutoField(primary_key=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    text = models.CharField(max_length=30)

    def __str__(self):
        return f"TextAnswer {self.text_id} for Answer {self.answer.answer_id}"