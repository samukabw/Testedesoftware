from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("marcar/<int:tarefa_id>/", views.marcar_feita, name="marcar_feita"),
    path('excluir/<int:tarefa_id>/', views.excluir_tarefa, name='excluir_tarefa'),

]
