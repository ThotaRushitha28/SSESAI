from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, "mainpage.html")

def pronounciation_view(request):
    return render(request, "pronounciation.html")

def vocabulary_view(request):
    return render(request, "vocabulary.html")

def word_scramble_view(request):
    return render(request, "word_scramble.html")

def speech_view(request):
    return render(request, "speech.html")

def speechspeed_view(request):
    return render(request, "speechspeed.html")

def quiz_view(request):
    return render(request, "quiz.html")

