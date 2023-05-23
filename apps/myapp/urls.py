from django.urls import path
from .views import hello, about

urlpatterns = [
    path('', hello),
    path('about/', about)
]
