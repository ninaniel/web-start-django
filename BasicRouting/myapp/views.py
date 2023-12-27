from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse("<h1 style='text-align: center;'>This is <span style='color: red;'>main</span> page.</h1>")

def home(request):
    return HttpResponse("<h2 style='text-align: center;'>This is <span style='font-style: italic;'>HOME</span> page.</h2>")

def contact(request):
    return HttpResponse("<h2 style='text-align: center;'>This is <span style='font-style: italic;'>CONTACT</span> page.</h2>")

def about(request):
    return HttpResponse("<h2 style='text-align: center;'>This is <span style='font-style: italic;'>ABOUT</span> page.</h2>")


