from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='masonMainPage'),
    path('Docs', views.docs, name='masonDocs')
]
