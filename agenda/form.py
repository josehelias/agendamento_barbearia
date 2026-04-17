from django import forms
from .models import Agendamento  

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ('barb_nome', 'servico', 'data', 'hora', 'client_nome', 'telefone')
            

    