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
from django.shortcuts import render, get_object_or_404, redirect

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def like_up(self,pk):
        question = get_object_or_404(Question, pk=pk)
        question.like +=1
        question.grade = question.like+question.dislike+question.conflict
        question.save()
        return redirect('/blog/question/')

    
    def dislike_up(self,pk):
        question = get_object_or_404(Question, pk=pk)
        question.dislike +=1
        question.grade +=1
        question.save()
        return redirect('/blog/question/')

    
    def conflict_up(self,pk):
        question = get_object_or_404(Question, pk=pk)
        question.conflict +=1
        question.grade +=1
        question.save()
        return redirect('/blog/question/')

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class Hall_of_FameViewSet(viewsets.ModelViewSet):
    queryset = Hall_of_Fame.objects.all()
    serializer_class = Hall_of_FameSerializer


class Top10ViewSet(viewsets.ModelViewSet):
    queryset = Top10.objects.all()
    serializer_class = Top10Serializer

    def top10check(self,pk):
        top10 = get_object_or_404(Top10, pk=pk)
        top10.tops ='ssss'
        top10.save()
        lists=Question.objects.order_by('-grade')
        toplen= 10 if len(lists)>10 else len(lists)
        tmp=(','.join(str(e) for e in lists[:toplen]))
        top10.tops =tmp
        return redirect('/blog/top10/')

