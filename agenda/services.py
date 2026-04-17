from datetime import datetime, timedelta
from .models import Disponibilidade, Agendamento

def gerar_horarios_disponiveis(barbeiro, data):
    dia_semana = data.weekday()

    disponibilidade = Disponibilidade.objects.filter(
        barbeiro=barbeiro,
        dia_semana = dia_semana
    ).first()

    if not disponibilidade:
        return []

    horarios = []
    hora_atual = datetime.combine(data, disponibilidade.hora_inicio)
    hora_final = datetime.combine(data, disponibilidade.hora_fim)

    intervalo_inicio = None
    intervalo_fim = None

    if disponibilidade.hora_inicio_intervalo and disponibilidade.hora_fim_intervalo:
        intervalo_inicio = datetime.combine(data, disponibilidade.hora_inicio_intervalo)
        intervalo_fim = datetime.combine(data, disponibilidade.hora_fim_intervalo)

    while hora_atual < hora_final:

        # Se existir intervalo e estiver dentro dele -> pulo
        if intervalo_inicio and intervalo_inicio <= hora_atual < intervalo_fim:
            hora_atual += timedelta(minutes=30)
            continue

        horarios.append(hora_atual.time())
        hora_atual += timedelta(minutes=30)

    # Separar para retornar só o que realmete está disponível

    agendados = set(
        Agendamento.objects.filter(
            barb_nome=barbeiro,
            data=data
        ).values_list('hora', flat=True)
    )

    horarios_disponiveis = [
        h for h in horarios if h not in agendados
    ]

    return horarios_disponiveis
