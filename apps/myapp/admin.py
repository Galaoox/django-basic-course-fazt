from django.contrib import admin
from .models import Project, Task

# Solo usando el admin.site.register se puede ver los modelos en el admin de django
admin.site.register(Project)
admin.site.register(Task)
