from django.shortcuts import render
from django.http import HttpResponse

def default_greeting(request):
    return HttpResponse("<h1 style='text-align: center'>Hello World!</h1>")

def greeting(request, name):
    return HttpResponse(f"<h2 style='text-align: center;'>Hello <span style='color: green;'>{name.title()}</span>!</h1>")
