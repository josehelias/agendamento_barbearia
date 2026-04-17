from django.db import models

# Create your models here.

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    duracao_minutos = models.IntegerField(default=30)

    def __str__(self):
        return self.nome

class Barbeiro(models.Model):
    barb_nome = models.CharField(max_length=100)

    def __str__(self):
        return self.barb_nome

class Disponibilidade(models.Model):
    DIAS_SEMANA = [
        (0, 'Segunda'),
        (1, 'Terça'),
        (2, 'Quarta'),
        (3, 'Quinta'),
        (4, 'Sexta'),
        (5, 'Sábado'),
        (6, 'Domingo'),
    ]

    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE)
    dia_semana = models.IntegerField(choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    hora_inicio_intervalo = models.TimeField(null=True, blank=True)
    hora_fim_intervalo = models.TimeField(null=True, blank=True)

class Agendamento(models.Model):
    client_nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateField(default=False)
    hora = models.TimeField(default=False)
    barb_nome = models.ForeignKey(Barbeiro, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('barb_nome', 'data', 'hora')
