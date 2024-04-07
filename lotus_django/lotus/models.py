from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



# # User		
# # UserID	Integer	NOT NULL, Primary Key, Auto Increment, Unique
# # Name	Varchar(60)	NOT NULL, encrypted
# # Email	Varchar(60)	NOT NULL, contains('@'), encrypted
# # Password	Varchar(255)	NOT NULL, Min 8, Hash
# # Colourscheme	Integer	NOT NULL, Default('white')
# # Admin	bool	NOT NULL, Default('false')

# # Entry		
# # EntryID	Integer	NOT NULL, Primary Key, Auto Increment, Unique
# # UserID	Integer	NOT NULL, Foreign Key(User)
# # Date	DateTime	NOT NULL, Auto Increment
# # is_journal	Bool	NOT NULL, Default('true')

# # Memory(Entry)

# # Memory		
# # MemoryID	Integer	NOT NULL, Primary Key, Auto Increment, Unique
# # EntryID	Integer	NOT NULL, Foreign Key(Entry)
# # Emotion	Varchar(40)	NOT NULL
# # Text	Varchar(60)	


# # Journal(Entry)	
# # Journal		
# # JournalID	Integer	NOT NULL, Primary Key, Auto Increment, Unique
# # EntryID	Integer	NOT NULL, Foreign Key(Entry)
# # Text	Mediumtext	encrypted

# # Question		
# # QuestionID	Integer	NOT NULL, Primary Key, Auto Increment, Unique
# # QuestionText	Varchar(255)	NOT NULL
# # QuestionType	Integer	NOT NULL
# # Active	bool	NOT NULL, Default('true')
# # Frequency	Varchar(20)	NOT NULL, Default('daily')

# # Answer		
# # AnswerID	Integer	NOT NULL, Primary Key, Auto Increment, Unique
# # QuestionID	Integer	NOT NULL, Foreign Key(Question)
# # UserID	Integer	NOT NULL, Foreign Key(User)
# # Date	DateTime	NOT NULL, Auto Increment

# # TextAnswer		
# # TextID	Integer	NOT NULL, Primary Key, Auto Increment, Unique
# # AnswerID	Integer	NOT NULL, Foreign Key(Answer)
# # text	Varchar(30)	encrypted

# # LikertAnswer		
# # LikertID	Integer	NOT NULL, Primary Key,  Auto Increment, Unique
# # AnswerID	Integer	NOT NULL, Foreign Key(Answer)
# # Value	Integer	


# # Questiontracker		
# # UserID	Integer	NOT NULL, Foreign Key(User), Primary Key
# # QuestionID	Integer	NOT NULL, Foreign Key(Question), Primary Key
# # Date	DateTime	NOT NULL

# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.utils import timezone

# # Create your models here.


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)

# class User(AbstractBaseUser):
#     user_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=60)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#     colourscheme = models.IntegerField(default=1)  # assuming 'white' is 1, other schemes can be assigned numbers accordingly
#     admin = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def __str__(self):
#         return self.email

# class Entry(models.Model):
#     entry_id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateTimeField(default=timezone.now)
#     is_journal = models.BooleanField(default=True)

#     def __str__(self):
#         return f"Entry {self.entry_id} by {self.user.email}"

# class Memory(models.Model):
#     memory_id = models.AutoField(primary_key=True)
#     entry_id = models.ForeignKey(Entry, on_delete=models.CASCADE)
#     emotion = models.CharField(max_length=40)
#     text = models.CharField(max_length=60)

#     def __str__(self):
#         return f"Memory {self.memory_id} for Entry {self.entry.entry_id}"

# class Journal(models.Model):
#     journal_id = models.AutoField(primary_key=True)
#     entry_id = models.ForeignKey(Entry, on_delete=models.CASCADE)
#     text = models.TextField()

#     def __str__(self):
#         return f"Journal {self.journal_id} for Entry {self.entry.entry_id}"

# class Question(models.Model):
#     question_id = models.AutoField(primary_key=True)
#     question_text = models.CharField(max_length=255)
#     question_type = models.IntegerField()
#     active = models.BooleanField(default=True)
#     frequency = models.CharField(max_length=20, default='daily')

#     def __str__(self):
#         return self.question_text
        
# class Answer(models.Model):
#     answer_id = models.AutoField(primary_key=True)
#     question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Answer {self.answer_id} by {self.user.email} for Question {self.question.question_id}"

# class TextAnswer(models.Model):
#     text_id = models.AutoField(primary_key=True)
#     answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
#     text = models.CharField(max_length=30)

#     def __str__(self):
#         return f"TextAnswer {self.text_id} for Answer {self.answer.answer_id}"
        
# class LikertAnswer(models.Model):
#     likert_id = models.AutoField(primary_key=True)
#     answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
#     value = models.IntegerField()

#     def __str__(self):
#     return f"LikertAnswer {self.likert_id} for Answer {self.answer.answer_id}"
# class QuestionTracker(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, primary_key=True)
#     date = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"QuestionTracker for User {self.user.user_id} and Question {self.question.question_id}"