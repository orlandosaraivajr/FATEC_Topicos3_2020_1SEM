from django.shortcuts import render
from django.http import HttpResponse

def natal(request):
    return HttpResponse('<h1>É Natal !</h1>')

