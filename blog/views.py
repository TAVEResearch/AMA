
from django.db.models.fields import NullBooleanField
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Question, Comment, Hall_of_Fame
from .forms import QuestionForm, CommentForm


from rest_framework import viewsets
from .serializers import *
from .models import *
from django.shortcuts import render, get_object_or_404, redirect



def index(request):
    return HttpResponse("안녕하세요 ama에 오신것을 환영합니다.")

def post(request):
    question_list = Question.objects.order_by('create_date')
    context = {'question_list': question_list}
    return render(request, 'post.html', context)

def question_display(request, question_id):
    try :
        question = Question.objects.get(id=question_id)
    except :
        return redirect('/blog/post') # question 없으니까 blog로 돌아가게 함

    comments = question.comment_set.all() # question에 연결된 comment들
    context = {"question":question, "comments":comments}
    return render(request, "question.html", context)

def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            if form.cleaned_data['vs_or_not'] == False: # vs_or_not unchecked : side_1, side_2 입력값무시
                question.side_1 = None
                question.side_2 = None
            question.create_date = timezone.now()
            question.like = 0
            question.dislike = 0
            question.conflict = 0
            question.save()
            return redirect('/blog/post/'+str(question.id)+'/')
    else:
        form = QuestionForm()
        context = {"form":form, "create":1}
        return render(request, "question_create.html", context)

def question_modify(request, question_id):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = Question.objects.get(id=question_id)
            question.subject = form.cleaned_data['subject']
            question.vs_or_not = form.cleaned_data['vs_or_not']
            question.side_1 = form.cleaned_data['side_1']
            question.side_2 = form.cleaned_data['side_2']
            if form.cleaned_data['vs_or_not'] == False: # vs_or_not unchecked : side_1, side_2 입력값무시
                question.side_1 = None
                question.side_2 = None
            question.save()
            return redirect('/blog/post/'+str(question_id)+'/')
    else:
        form = QuestionForm()
        question = Question.objects.get(id=question_id)
        context = {"form":form, "create":0, "question":question}
        return render(request, "question_create.html", context)
            
def question_delete(request, question_id):
    question = Question.objects.get(id=question_id)
    question.delete()
    return redirect('/blog/post/')

def comment_create(request, question_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.question_id = question_id
            comment.create_date = timezone.now()
            comment.save()
            return redirect('/blog/post/', question_id=comment.question_id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'comment_create.html', context)

def comment_modify(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_date = timezone.now()  # 수정일시 저장
            comment.save()
            return redirect('/blog/post/', question_id=comment.question_id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'comment_create.html', context)

def comment_delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('/blog/post/', question_id=comment.question_id)

def hall_of_fame(request):
    questions = Question.objects.all()
    Hall_of_Fame.objects.all().delete()
    for question in questions:
        like = question.like
        dislike = question.dislike
        conflict = question.conflict
        res_sum = like + dislike + conflict

        if res_sum >= 0:
            Hall_of_Fame.objects.create(question=Question(id=question.id), response=res_sum)

    hall_of_fame = Hall_of_Fame.objects.order_by('-response')
    value_list = []

    for value in hall_of_fame:
        question = Question.objects.get(id=value.question_id)
        value_list.append(question)

    context = {"hall_of_fame": value_list}
    return render(request, 'hall_of_fame.html', context)




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
        # top10.tops ='ssss'
        lists=Question.objects.order_by('-grade')
        toplen= 10 if len(lists)>10 else len(lists)
        tmp=(','.join(str(e) for e in lists[:toplen]))
        top10.tops = tmp
        top10.save()

        print(top10.tops)
        return redirect('/blog/top10/')
