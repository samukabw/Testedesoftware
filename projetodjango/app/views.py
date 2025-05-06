from django.shortcuts import render,redirect, get_object_or_404
from .models import Tarefa


def index(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        descricao = request.POST.get("descricao", "").strip()
        if titulo:
            Tarefa.objects.create(titulo=titulo,descricao=descricao)
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