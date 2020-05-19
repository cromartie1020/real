from django.shortcuts import render
import pages

def index(request):
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html')    