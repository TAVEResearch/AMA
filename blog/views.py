from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 ama에 오신것을 환영합니다.")

def post(request):
    return HttpResponse("post")

def hall_of_fame(request):
    return HttpResponse("hall-of-fame")
