from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime, date
from django.template import loader
from .models import Barbeiro, Servico
from .services import gerar_horarios_disponiveis

def agendamentos(request):
    barbeiros = Barbeiro.objects.all().values()
    Servicos = Servico.objects.all().values()
    template = loader.get_template('agendar.html')
    context = {
        'barbeiros': barbeiros,
        'servicos': Servicos,
        'hoje': date.today().strftime("%Y-%m-%d")
    }
    return HttpResponse(template.render(context, request))

def buscar_horarios(request):
    barbeiro_id = request.GET.get('barbeiro_id')
    data_selecionada = request.GET.get('data')

    data = datetime.strptime(data_selecionada, "%Y-%m-%d").date()
    barbeiro = Barbeiro.objects.get(id=barbeiro_id)

    horarios = gerar_horarios_disponiveis(barbeiro, data)

    return JsonResponse({
        "horarios": [h.strftime("%H:%M") for h in horarios]
    })


