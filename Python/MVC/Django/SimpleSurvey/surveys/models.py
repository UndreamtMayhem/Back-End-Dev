from django.db import models

# Create your models here.
class Survey(models.Model):
    title = models.CharField(max_length = 200)
    def __str__(self):
        return self.title

class Question(models.Model):
    question_text = models.CharField(max_length = 900)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.choice_text


class SurveyAnswer(models.Model):
    orig_survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

class QuestionAnswer(models.Model):
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE)
    survey_answer = models.ForeignKey(SurveyAnswer, on_delete=models.CASCADE)
