from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home/ppHome.html', {})

def docs(request):
    return render(request, 'docs/ppDocs.html', {})

def projects(request):
    return render(request, 'projects/ppProjects.html', {})

def goToLinkedIn(request):
    linkedinURL = "https://linkedin.com/in/mason-you-1057401a0"
    return redirect(linkedinURL)

def goToGitHub(request):
    githubURL = "https://github.com/MasonYou"
    return redirect(githubURL)
