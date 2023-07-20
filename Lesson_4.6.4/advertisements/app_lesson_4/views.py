from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def les4(requests):
    return HttpResponse("Домашка по 4 занятию")