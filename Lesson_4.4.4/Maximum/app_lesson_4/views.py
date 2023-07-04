from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def lesson_4(request):
    return HttpResponse("Домашка по 4 занятию")

def main(request):
    return HttpResponse("Переключитесь на http://127.0.0.1:8000/lesson_4")