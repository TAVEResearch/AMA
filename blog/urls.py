from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('post/', views.post),
    path('post/<int:question_id>/', views.question_display),
    path('post/question/', views.question_create),
    path('post/<int:question_id>/comment/', views.comment_create),
    path('post/<int:comment_id>/comment-modify/', views.comment_modify),
    path('post/<int:comment_id>/comment-delete/', views.comment_delete),
    path('hall-of-fame/', views.hall_of_fame),
]
