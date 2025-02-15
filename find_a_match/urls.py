from django.urls import path
from . import views

urlpatterns = [
    path('', views.find_a_match, name='find_a_match'),
]