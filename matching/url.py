from django.urls import path
from .views import find_a_match

urlpatterns = [
    path('', views.find_a_match, name='find_a_match'),
]

