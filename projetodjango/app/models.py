from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True) 
    feita = models.BooleanField(default=False)
    data_hora = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.titulo
