from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    # de esta forma se hacen las relaciones entre tablas y se usa la eliminacion en cascada
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
