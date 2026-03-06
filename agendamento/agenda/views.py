from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib import messages
from datetime import datetime

from .models import Barbeiro, Servico
from .services import gerar_horarios_disponiveis
from .form import AgendamentoForm

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))

def servicos(request):
    template = loader.get_template('serviços.html')
    Servicos = Servico.objects.all().values()
    return HttpResponse(template.render({'servicos': Servicos}, request))


def agendamentos(request):
    if request.method == 'POST':
        # Aqui o formulário recebe os dados digitados + o ID do serviço que vira do campo hidden
        form = AgendamentoForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Agendamento realizado com sucesso! Esperamos por você.')
            return redirect('agendamentos') # Redireciona para a página de agendamento, onde o form será exibido novamente
        else:
            # Se houver erro, precisamos recarregar os barbeiros para o template não quebrar
            barbeiros = Barbeiro.objects.all().values()
            return redirect('agendamentos') # Redireciona para a página de agendamento, onde o form será exibido novamente

    elif request.method == 'GET':
        servico_id = request.GET.get('servico')
        # Criamos o form com o serviço pré-preenchido
        form = AgendamentoForm(initial={'servico': servico_id})
        barbeiros = Barbeiro.objects.all().values()
        
        return render(request, 'agendar.html', {
            'barbeiros': barbeiros,
            'form': form,
            'servico_id': servico_id # Passamos o ID para o template
        })
    else:
        servicos() # Se for outro método, redirecionamos para a página de serviços

        
    
def buscar_horarios(request):
    barbeiro_id = request.GET.get('barbeiro_id')
    data_selecionada = request.GET.get('data')

    data = datetime.strptime(data_selecionada, "%Y-%m-%d").date()
    barbeiro = Barbeiro.objects.get(id=barbeiro_id)

    horarios = gerar_horarios_disponiveis(barbeiro, data)

    return JsonResponse({
        "horarios": [h.strftime("%H:%M") for h in horarios]
    })


