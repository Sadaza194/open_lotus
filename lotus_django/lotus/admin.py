from django.contrib import admin
from lotus.user import User
from lotus.user import CustomUserManager
from lotus.entry import Entry
from lotus.entryChilds import Memory
from lotus.entryChilds import Journal
from lotus.question import Question
from lotus.answer import Answer
from lotus.textAnswer import TextAnswer
from lotus.likertAnswer import LikertAnswer
from lotus.questionTracker import QuestionTracker

# Register your models here.
admin.site.register(User)
admin.site.register(Entry)
admin.site.register(Memory)
admin.site.register(Journal)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(TextAnswer)
admin.site.register(LikertAnswer)
admin.site.register(QuestionTracker)