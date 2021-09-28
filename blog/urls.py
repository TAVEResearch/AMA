from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('post/', views.post),
    path('post/<int:question_id>/', views.question_display),
    path('post/question/', views.question_create),
    path('post/comment/<int:question_id>/', views.comment_create),
    path('hall-of-fame/', views.hall_of_fame),
]
