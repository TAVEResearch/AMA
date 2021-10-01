from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from .models import Question, Comment
from .forms import QuestionForm, CommentForm



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
        return redirect('/blog/') # question 없으니까 blog로 돌아가게 함

    comments = question.comment_set.all() # question에 연결된 comment들
    context = {"question":question, "comments":comments}
    return render(request, "question.html", context)

def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.like = 0
            question.dislike = 0
            question.conflict = 0
            question.save()
            return redirect('/blog/')
    else:
        form = QuestionForm()
        context = {"form":form}
        return render(request, "question_create.html", context)

def comment_create(request, question_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.question_id = question_id
            comment.create_date = timezone.now()
            comment.save()
            return redirect('/blog/post/')
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

def hall_of_fame(request):
    questions = Question.objects.all()
    for question in questions:
        print(question)
    return HttpResponse("안녕하세요 ama에 오신것을 환영합니다.")