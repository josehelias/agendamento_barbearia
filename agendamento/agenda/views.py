from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime, date
from django.template import loader
from .models import Barbeiro, Servico
from .services import gerar_horarios_disponiveis
from .form import AgendamentoForm

def agendamentos(request):
    if request.method == 'POST':
        print("0")
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            print("1")
            form.save()
            return HttpResponse("Agendamento realizado com sucesso!")
        else:
            return HttpResponse("Erro no formulário. Verifique os dados e tente novamente.")
    else:
        print("2")
        form = AgendamentoForm()
        barbeiros = Barbeiro.objects.all().values()
        Servicos = Servico.objects.all().values()
        template = loader.get_template('agendar.html')
        context = {
            'barbeiros': barbeiros,
            'servicos': Servicos,
            'hoje': date.today().strftime("%Y-%m-%d"),
            'form': form
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


