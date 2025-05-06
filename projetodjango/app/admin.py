from django.contrib import admin
from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'feita')
    search_fields = ('titulo',)
    list_filter = ('feita',)
