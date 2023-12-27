from django.shortcuts import render
from django.http import HttpResponse

def empty_entry(request):
    return HttpResponse("<h1 style= 'text-align: center;'>Please add any number.</p>")

def odd_even(request, num):
    result = "even" if num % 2 == 0 else "odd"
    return HttpResponse(f"<h1 style= 'text-align: center;'>This number is <span style='color: green;'>{result}</span>.")