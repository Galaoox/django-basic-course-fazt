from django.urls import path
from .views import hello, about, index

urlpatterns = [
    path('', index),
    path('about/', about),
    # de esta forma se pasan parametros a la url, se debe definir el tipo del parametro
    path('hello/<str:username>', hello),
]
