
from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    vs_or_not = models.BooleanField(default=True)
    side_1 = models.CharField(max_length=200)
    side_2 = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    like = models.IntegerField()
    dislike = models.IntegerField()
    conflict = models.IntegerField()

class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comment = models.TextField()
    create_date = models.DateTimeField()

class Hall_of_Fame(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)



class Top10(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    grade = models.IntegerField()
    rank = models.FloatField()