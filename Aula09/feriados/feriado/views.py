from django.shortcuts import render
from django.http import HttpResponse

def natal(request):
    return render(request, 'natal.html')

