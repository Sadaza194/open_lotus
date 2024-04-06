from django.db import models

# Create your models here.


class Question(models.Model):
    text = models.TextField(max_length=255, null=False)
    type = models.IntegerField(null=False)
    active = models.BooleanField(default=True, null=False)
    frequency = models.CharField(max_length=20, null=False, default="daily")

# # Question		
# # QuestionID	Integer	NOT NULL, Primary Key, Auto Increment, Unique
# # QuestionText	Varchar(255)	NOT NULL
# # QuestionType	Integer	NOT NULL
# # Active	bool	NOT NULL, Default('true')
# # Frequency	Varchar(20)	NOT NULL, Default('daily')