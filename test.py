import io
import unittest
from unittest.mock import patch
from main import (
    get_valid_name,
    get_valid_subject,
    get_valid_grade,
    class_media,
    call_menu
)

class TestStudentSystem(unittest.TestCase):

    # Testes para get_valid_name()
    def test_get_valid_name_immediate_valid(self):
        # Nome válido na primeira tentativa
        with patch('builtins.input', return_value="John Doe"):
            result = get_valid_name()
            self.assertEqual(result, "John Doe")

    def test_get_valid_name_invalid_then_valid(self):
        # Tenta um nome inválido (contendo dígitos) e depois um nome válido
        inputs = ["Jo4hn", "John Doe"]
        with patch('builtins.input', side_effect=inputs):
            result = get_valid_name()
            self.assertEqual(result, "John Doe")
    
    # Testes para get_valid_subject()
    def test_get_valid_subject_single(self):
        # Cadastro de apenas uma matéria
        inputs = ["Matemática", "n"]
        materias = []
        with patch('builtins.input', side_effect=inputs):
            result = get_valid_subject(materias)
            self.assertEqual(result, ["Matemática"])
    
    def test_get_valid_subject_multiple(self):
        # Cadastro de múltiplas matérias
        inputs = ["Matemática", "s", "História", "n"]
        materias = []
        with patch('builtins.input', side_effect=inputs):
            result = get_valid_subject(materias)
            self.assertEqual(result, ["Matemática", "História"])
    
    # Testes para get_valid_grade()
    def test_get_valid_grade_all_valid(self):
        # Cadastro de 4 notas válidas direto
        inputs = ["80", "90", "70", "60"]
        with patch('builtins.input', side_effect=inputs):
            result = get_valid_grade()
            self.assertEqual(result, [80.0, 90.0, 70.0, 60.0])
    
    def test_get_valid_grade_invalid_then_valid(self):
        # Para a 1ª nota, insere entrada inválida ("abc") e depois válida ("80")
        inputs = ["abc", "80", "90", "70", "60"]
        with patch('builtins.input', side_effect=inputs):
            result = get_valid_grade()
            self.assertEqual(result, [80.0, 90.0, 70.0, 60.0])
    
    # Testes para class_media()
    def test_class_media_excellent(self):
        # Média 95 -> "Excelente!"
        result = class_media([95, 95, 95, 95], "Test Student")
        self.assertIn("Classificação: Excelente!", result)
    
    def test_class_media_good(self):
        # Média 75 -> "Bom!"
        result = class_media([75, 75, 75, 75], "Test Student")
        self.assertIn("Classificação: Bom!", result)
    
    def test_class_media_regular(self):
        # Média 60 -> "Regular!"
        result = class_media([60, 60, 60, 60], "Test Student")
        self.assertIn("Classificação: Regular!", result)
    
    def test_class_media_needs_improvement(self):
        # Média 40 -> "Precisa ser melhor!"
        result = class_media([40, 40, 40, 40], "Test Student")
        self.assertIn("Classificação: Precisa ser melhor!", result)
    
    # Testes para call_menu() – Integração do sistema
    def test_call_menu_invalid_option(self):
        """
        Simula a entrada de uma opção inválida (não numérica) para o menu, 
        seguido da escolha para sair (opção 5).
        """
        inputs = [
            "abc",  # Opção inválida: não numérica.
            "",     # Pressione Enter para continuar.
            "5"     # Opção para sair.
        ]
        with patch('builtins.input', side_effect=inputs), \
             patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            call_menu("", [], [])
            output = fake_out.getvalue()
            self.assertIn("Opção inválida! Digite um número de 1 a 5.", output)
            self.assertIn("Saindo do programa", output)
    
    def test_call_menu_integration(self):
        """
        Testa o fluxo completo do sistema interativo:
          1. Cadastro de Aluno (nome: "Alice")
          2. Cadastro de Matéria (adiciona "Matemática" e "História")
          3. Cadastro de Notas (80, 90, 70, 60)
          4. Exibição da Média e Classificação
          5. Saída do sistema
        """
        inputs = [
            "1",           # Opção 1: Cadastrar Aluno
            "Alice",       # Nome do aluno
            "",            # Pressione Enter para continuar

            "2",           # Opção 2: Cadastrar Matéria
            "Matemática",  # 1ª matéria
            "s",           # Deseja adicionar outra matéria
            "História",    # 2ª matéria
            "n",           # Encerra o cadastro de matérias
            "",            # Pressione Enter para continuar

            "3",           # Opção 3: Cadastrar Notas
            "80",          # 1ª nota
            "90",          # 2ª nota
            "70",          # 3ª nota
            "60",          # 4ª nota
            "",            # Pressione Enter para continuar

            "4",           # Opção 4: Exibir Média e Classificação
            "",            # Pressione Enter para continuar

            "5"            # Opção 5: Sair
        ]
        with patch('builtins.input', side_effect=inputs), \
             patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            call_menu("", [], [])
            output = fake_out.getvalue()
            # Verifica se os principais blocos aparecem na saída:
            self.assertIn("Cadastro de Aluno", output)
            self.assertIn("Aluno cadastrado com sucesso", output)
            self.assertIn("Cadastro de Matéria", output)
            self.assertIn("Matéria(s) cadastrada(s) com sucesso", output)
            self.assertIn("Cadastro de Notas", output)
            self.assertIn("Notas cadastradas com sucesso", output)
            self.assertIn("Média e Classificação do Aluno", output)
            self.assertIn("Classificação:", output)
            self.assertIn("Saindo do programa", output)

if __name__ == "__main__":
    unittest.main()
