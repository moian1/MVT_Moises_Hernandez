from django.shortcuts import render

from Miapp.models import familiares

# Create your views here.

def mostrar_Familiares(request):
    padre = familiares(nombre="Brigido ", apellido=" Hernandez", edad=65, cumpleaños="14/08/1957")
    madre = familiares(nombre=" Roselia ", apellido=" Quintero", edad=50, cumpleaños="20/06/1962")
    hermano = familiares(nombre="Marco ", apellido=" Hernandez", edad=28, cumpleaños="19/05/1992")


    return render(request, "familiares.html", {"amigos":[padre, madre, hermano]})

