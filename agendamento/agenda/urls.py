from django.urls import path
from . import views

urlpatterns = [
    path('agendamentos/', views.agendamentos, name='agendamentos'),
    path('buscar-horarios/', views.buscar_horarios, name='buscar_horarios'),
]
