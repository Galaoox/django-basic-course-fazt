# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h1> Index page </h1>")


def hello(request, username):  # de esta forma se reciben los parametros que vienen de la url en la vista
    return HttpResponse(f'<h1> Hello world {username} </h1>')


def about(request):
    return HttpResponse("<h1> About page ! </h1>")
