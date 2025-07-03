from django.shortcuts import render
from django.shortcuts import redirect


from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenue sur la page d'accueil de l'application  !")

def index(request):
    return redirect('/admin/login/')

