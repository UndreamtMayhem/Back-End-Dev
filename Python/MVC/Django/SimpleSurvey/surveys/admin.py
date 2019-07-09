from django.contrib import admin

# Register your models here.

from .models import Survey, Question, Choice, SurveyAnswer, QuestionAnswer

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(SurveyAnswer)
admin.site.register(QuestionAnswer)