from django.urls import path

from . import views

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = format_suffix_patterns([


    path('', views.index),
    path('post/', views.post),
    path('post/<int:question_id>/', views.question_display),
    path('post/question/', views.question_create),

    path('post/<int:question_id>/question-modify', views.question_modify),
    path('post/<int:question_id>/question-delete', views.question_delete),

    path('post/<int:question_id>/comment/', views.comment_create),
    path('post/<int:comment_id>/comment-modify/', views.comment_modify),
    path('post/<int:comment_id>/comment-delete/', views.comment_delete),
    path('hall-of-fame/', views.hall_of_fame),






    # question
    path('question/', QuestionViewSet.as_view({
        'post': 'create',
        'get': 'list'
    })),
    path('question/<int:pk>/',QuestionViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),

    path('question/<int:pk>/like/',QuestionViewSet.like_up),
    path('question/<int:pk>/dislike/',QuestionViewSet.dislike_up),
    path('question/<int:pk>/conflict/',QuestionViewSet.conflict_up),


    # comment
    path('comment/', CommentViewSet.as_view({
        'get': 'list'
    })),
    path('comment/create/<int:pk>/', CommentViewSet.as_view({
        'post': 'create'
    })),

    path('comment/<int:pk>/', CommentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update'
    })),

    path('comment/delete/<int:pk>/', CommentViewSet.as_view({
        'delete': 'destroy'
    })),


    # Hall_of_Fame
    path('hall/', Hall_of_FameViewSet.as_view({
        'get': 'list'
    })),
    path('hall/create/<int:pk>/', Hall_of_FameViewSet.as_view({
        'post': 'create'
    })),

    path('hall/<int:pk>/', Hall_of_FameViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update'
    })),

    path('hall/delete/<int:pk>/', Hall_of_FameViewSet.as_view({
        'delete': 'destroy'
    })),


 # top
    path('top10/', Top10ViewSet.as_view({
        'post': 'create',
        'get': 'list'
    })),

    # path('top10/<int:pk>/', Top10ViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'patch': 'partial_update',
    #     'delete': 'destroy'
        
    # })),
    path('top10/<int:pk>/', Top10ViewSet.top10check),

    

])