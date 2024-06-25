from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home/ppHome.html', {})

def docs(request):
    return render(request, 'docs/ppDocs.html', {})