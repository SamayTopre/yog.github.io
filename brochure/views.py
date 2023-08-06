from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

def videos(request):
    return render(request,'videos.html')

def brochure(request):
    return render(request,'brochure.html')

