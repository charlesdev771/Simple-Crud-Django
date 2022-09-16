from django.contrib import admin
from django.urls import path, include 
from .views import home
from .views import salvar, editar, update, delete

urlpatterns = [
    path('', home),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('salvar/', salvar, name="salvar"),
    path('delete/<int:id>', delete, name="delete"),
]
 