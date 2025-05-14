from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Tarefa

class TestMyView(TestCase):
    def test_view_status_code(self):
        response = self.client.get(reverse('index'))  # Nome da view ou URL
        self.assertEqual(response.status_code, 200)



class TarefaModelTest(TestCase):

    def test_create_tarefa(self):
        tarefa = Tarefa.objects.create(
            titulo="Estudar Django", descricao="Revisar testes", data_hora=timezone.now()
        )
        self.assertEqual(tarefa.titulo, "Estudar Django")
        self.assertEqual(tarefa.descricao, "Revisar testes")
        self.assertIsNotNone(tarefa.data_hora)





class URLTest(TestCase):

    def setUp(self):
        # Cria uma tarefa para testar a exclusão
        self.tarefa = Tarefa.objects.create(
            titulo="Testar exclusão",
            descricao="Teste de exclusão de tarefa",
            data_hora=None  # Caso não precise da data e hora
        )

    def test_excluir_url(self):
        response = self.client.post(reverse('excluir_tarefa', args=[self.tarefa.id]))  # Usando a tarefa criada no setUp
        self.assertEqual(response.status_code, 302)  # Esperando o redirecionamento após a exclusão
