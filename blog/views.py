# from django.http.response import HttpResponseRedirect
# from django.shortcuts import render
# from django.http import HttpResponse

# from .models import Question, Top10
# from django.utils import timezone
# from .forms import QuestionForm, Top10Form
# from django.shortcuts import redirect

from rest_framework import viewsets
from .serializers import *
from .models import *


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class Hall_of_FameViewSet(viewsets.ModelViewSet):
    queryset = Hall_of_Fame.objects.all()
    serializer_class = Hall_of_FameSerializer

class Top10ViewSet(viewsets.ModelViewSet):
    queryset = Top10.objects.all()
    serializer_class = Top10Serializer

