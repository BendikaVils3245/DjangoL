from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse('<h1>Текст</h1>')

def about(request):
    return HttpResponse('<h2>Второй текст</h2>')

