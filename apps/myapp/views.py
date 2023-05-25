# from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render


# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def hello(request, username):  # de esta forma se reciben los parametros que vienen de la url en la vista
    return HttpResponse(f'<h1> Hello world {username} </h1>')


def projects(request):
    projects = list(Project.objects.all().values())
    return render(request, 'projects.html')


def tasks(request):
    # se puede usar estas funciones de django para obtener un objeto o un 404
    # task = get_object_or_404(Task, id=id)
    return render(request, 'tasks.html')
