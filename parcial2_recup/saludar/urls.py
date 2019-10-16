
from django.urls import path

from . import views


urlpatterns = [
    path('hola/<nombre>', views.hola, name='hola'),
]
