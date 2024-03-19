from django.db import models
from .user import User
from .question import Question

class QuestionTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"QuestionTracker for User {self.user.user_id} and Question {self.question.question_id}"