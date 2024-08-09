from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:pais_medalhas>', views.atletas_medalhas, name="atletas_medalhas"),
    
]