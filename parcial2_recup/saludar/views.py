from django.shortcuts import render
from .models import Greet, Name
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404


def hola(request, nombre):
    return HttpResponse("Hola, " + nombre )
