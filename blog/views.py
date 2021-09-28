from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

from .models import Question
from django.utils import timezone
from .forms import QuestionForm
from django.shortcuts import redirect


def index(request):
    return HttpResponse("안녕하세요 ama에 오신것을 환영합니다.")

def post(request):
    return HttpResponse("post")

def hall_of_fame(request):
    return HttpResponse("hall-of-fame")



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
            question.save()
            return redirect('/blog/post/'+str(question_id)+'/')
    else:
        form = QuestionForm()
        context = {"form":form, "create":0}
        return render(request, "question_create.html", context)
            
def question_delete(request, question_id):
    question = Question.objects.get(id=question_id)
    question.delete()
    return redirect('/blog/')