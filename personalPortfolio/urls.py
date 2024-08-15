from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='masonMainPage'),
    path('Docs', views.docs, name='masonDocs'),
    path('Projects', views.projects, name='masonProjects'),
    path('masonlinkedin', views.goToLinkedIn, name='goToLinkedIn'),
    path('masongithub', views.goToGitHub, name='goToGitHub')
]
