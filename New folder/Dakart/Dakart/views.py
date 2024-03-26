
from django.http import HttpResponse
from django.shortcuts import render

def welcomescreen(request):
    return render(request,'welcome.html')