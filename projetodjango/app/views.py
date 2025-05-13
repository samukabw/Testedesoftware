from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from django.utils.dateparse import parse_datetime

def index(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        descricao = request.POST.get("descricao", "").strip()
        data_hora = request.POST.get("horario")  # Agora usando "horario", que é o nome do campo no HTML
        horario = parse_datetime(data_hora) if data_hora else None
        if titulo:
            Tarefa.objects.create(titulo=titulo, descricao=descricao, data_hora=horario)
        return redirect("index")

    tarefas = Tarefa.objects.all().order_by("feita")
    return render(request, "app/index.html", {"tarefas": tarefas})

def marcar_feita(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    tarefa.feita = not tarefa.feita
    tarefa.save()
    return redirect("index")

def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    tarefa.delete()
    return redirect("index")
