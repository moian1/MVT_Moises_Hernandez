from django.urls import path

from Miapp.views import mostrar_Familiares


urlpatterns = [
    path('', mostrar_Familiares)
]