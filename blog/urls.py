from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('post/', views.post),
    path('hall-of-fame/', views.hall_of_fame),

    path('post/<int:question_id>/', views.question_display),
    path('post/question/', views.question_create),

    path('post/<int:question_id>/question-modify', views.question_modify),
    path('post/<int:question_id>/question-delete', views.question_delete),
]

#test