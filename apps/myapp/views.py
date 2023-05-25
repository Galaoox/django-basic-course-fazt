# from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404


# Create your views here.


def index(request):
    return HttpResponse("<h1> Index page </h1>")


def hello(request, username):  # de esta forma se reciben los parametros que vienen de la url en la vista
    return HttpResponse(f'<h1> Hello world {username} </h1>')


def about(request):
    return HttpResponse("<h1> About page ! </h1>")


def projects(request):
    projects = list(Project.objects.all().values())
    return JsonResponse(projects, safe=False)


def tasks(request, id):
    # se puede usar estas funciones de django para obtener un objeto o un 404
    task = get_object_or_404(Task, id=id)
    return HttpResponse(f'<h1> Task: {task.title} </h1>')
