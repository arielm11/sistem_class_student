# 📊 Sistema de Classificação de Alunos  
Este projeto é um sistema simples para classificação de alunos com base em suas notas. Ele solicita o nome do aluno, valida as notas inseridas e calcula a média, exibindo uma classificação final.  

## 🎯 Objetivo  
O objetivo principal do projeto é:  

- Permitir que um usuário informe o nome, as matérias e  as notas de um aluno.  
- Garantir que apenas nomes válidos (sem números ou caracteres especiais) sejam aceitos.  
- Validar as notas, permitindo apenas valores numéricos.  
- Calcular a média e exibir a classificação do aluno.  

## ⚙️ Funcionalidades  
✅ **Validação de Nome**: O sistema verifica se o nome contém apenas letras e espaços.  
✅ **Validação de Notas**: Apenas números são aceitos como nota.  
✅ **Cálculo da Média**: Calcula a média com base em quatro notas.  
✅ **Classificação do Aluno**: A média define a classificação:  
   - **Excelente** (Média ≥ 90)  
   - **Bom** (Média entre 70 e 89)  
   - **Regular** (Média entre 50 e 69)  
   - **Precisa ser melhor** (Média < 50)  

## 📋 Pré-requisitos  
Antes de executar o programa, você precisará ter:  
- **Python 3.x** instalado no seu sistema.  

## 📁 Estrutura do Projeto  
- **`main.py`**: Código principal do sistema.  
- **`test.py`**: Arquivo de testes automatizados (se houver).  
- **`README.md`**: Documentação do projeto.

## 🔧 Como Usar  
1️.Clone este repositório:  
```bash
git clone https://github.com/seuusuario/sistema-classificacao-alunos.git
cd sistema-classificacao-alunos
```
2.Execute o script principal:
```bash
python main.py
```
3.Insira os dados solicitados e veja a classificação do aluno.

## 🖥️ Tecnologias Utilizadas
- **Python:** Linguagem principal do projeto.
- **Regex (re do Python):** Para validação de entrada de dados.
- **unittest:** Framework nativo para criação e execução de testes unitários.
- **unittest.mock:** Para simular entradas (patch do `input()`) e capturar saídas (patch do `sys.stdout`).
- **io.StringIO:** Utilizado para armazenar e analisar a saída do programa em memória.