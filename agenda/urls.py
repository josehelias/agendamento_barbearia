from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agendamentos/', views.servicos, name='agendamentos'),
    path('servicos/', views.servicos, name='servicos'),
    path('contato/', views.contato, name='contato'),
    path('buscar-horarios/', views.buscar_horarios, name='buscar_horarios'),
]
