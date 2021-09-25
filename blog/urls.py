from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('post/', views.post),
    path('hall-of-fame/', views.hall_of_fame),
]