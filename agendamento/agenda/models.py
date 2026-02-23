from django.db import models

# Create your models here.

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    duracao_minutos = models.IntergerField(default=30)

    def __str__(self):
        return self.nome

class Atendente(models.Model):
    atend_nome = models.CharField(max_length=100)

class Agendamento(models.Model):
    client_nome = models.CharField(max_length=100)
    telefone = models.CharField(max_lenght=20, blank=True)
    servico = models.FereignKey(Servico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(default=False)
    atendente = models.ForeignKey(Atendente, on_delete=models.CASCADE)

