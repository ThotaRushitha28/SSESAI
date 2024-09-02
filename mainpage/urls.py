from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="mainpage"),
    path("pronounciation/", views.pronounciation_view, name="pronounciation"),
    path("vocabulary/", views.vocabulary_view, name="vocabulary"),
    path("word_scramble/", views.word_scramble_view, name="word_scramble"),
    path("speech/", views.speech_view, name="speech"),
    path("speechspeed/", views.speechspeed_view, name="speechspeed"),
    path("quiz/", views.quiz_view, name="quiz"),
]