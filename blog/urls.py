from django.urls import path

from . import views

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

# question_list = QuestionViewSet.as_view({
#     'post': 'create',
#     'get': 'list'
# })

# question_detail = QuestionViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# question_list = QuestionViewSet.as_view({
#     'post': 'create',
#     'get': 'list'
# })

# question_detail = QuestionViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })


# question_list = QuestionViewSet.as_view({
#     'post': 'create',
#     'get': 'list'
# })

# question_detail = QuestionViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })


# question_list = QuestionViewSet.as_view({
#     'post': 'create',
#     'get': 'list'
# })

# question_detail = QuestionViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })



urlpatterns = format_suffix_patterns([
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


 # comment
    path('top10/', Top10ViewSet.as_view({
        'get': 'list'
    })),
    path('top10/create/<int:pk>/', Top10ViewSet.as_view({
        'post': 'create'
    })),

    path('top10/<int:pk>/', Top10ViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update'
    })),

    path('top10/delete/<int:pk>/', Top10ViewSet.as_view({
        'delete': 'destroy'
    })),




])
