from django.contrib import admin
from .models import Servico, Barbeiro, Disponibilidade, Agendamento

# Register your models here.

admin.site.register([Servico, Barbeiro, Disponibilidade, Agendamento])
