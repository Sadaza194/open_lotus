from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    type = models.CharField(null=False, max_length=20)
    text = models.TextField()
    frequency = models.CharField(max_length=20, null=False, default="daily")
    active = models.BooleanField(default=True, null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class QuestionTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    
class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    
class LikertAnswer(models.Model):
    likert_id = models.AutoField(primary_key=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    value = models.IntegerField()


class TextAnswer(models.Model):
    text_id = models.AutoField(primary_key=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    text = models.CharField(max_length=30)
