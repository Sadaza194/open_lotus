from django.contrib import admin
from questions.models import Question
from questions.models import QuestionTracker
from questions.models import LikertAnswer
from questions.models import TextAnswer

# Register your models here.
admin.site.register(Question)
admin.site.register(QuestionTracker)
admin.site.register(LikertAnswer)
admin.site.register(TextAnswer)
