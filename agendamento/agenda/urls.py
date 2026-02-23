from django.urls import path
from . import views

urlpatterns = [
    path('agendamentos/', views.agendamentos, name='agendamentos'),
]
