from django.db import models


class Question(models.Model):
    pass

class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comment = models.TextField()
    create_date = models.DateTimeField()

class Hall_of_Fame(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)