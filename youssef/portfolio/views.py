from django.shortcuts import render

def index(request):
    return render(request,'portfolio/index.html')

def photo(request):
    return render(request,'portfolio/photo.html')

def developer(request):
    return render(request,'portfolio/developer.html')
