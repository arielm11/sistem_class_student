import re

# Códigos de cores para o terminal (ANSI escape codes)
RED    = '\033[31m'
GREEN  = '\033[32m'
YELLOW = '\033[33m'
BLUE   = '\033[34m'
CYAN   = '\033[36m'
RESET  = '\033[0m'
BOLD   = '\033[1m'

# Variáveis globais
nome = ""
notas = []
materias = []

def print_header():
    print(BLUE + "=" * 60)
    print(BOLD + "SISTEMA DE CLASSIFICAÇÃO DE ALUNOS".center(60))
    print("=" * 60 + RESET)

def print_menu():
    print("\n" + CYAN + "Menu Principal".center(60) + RESET)
    print("-" * 60)
    print("1 - Cadastrar Aluno")
    print("2 - Cadastrar Matéria")
    print("3 - Cadastrar Notas")
    print("4 - Exibir Média e Classificação")
    print("5 - Sair")
    print("-" * 60)

def call_menu(nome, notas, materias):
    while True:
        print_header()
        print_menu()
        try:
            opcao = int(input(YELLOW + "\nDigite a opção desejada: " + RESET))
        except ValueError:
            print(RED + "\nOpção inválida! Digite um número de 1 a 5." + RESET)
            input("\nPressione Enter para continuar...")
            continue

        if opcao == 1:
            print("\n" + BLUE + "Cadastro de Aluno".center(60) + RESET)
            print("Digite os dados do aluno abaixo:")
            nome = get_valid_name()
            print(GREEN + "\nAluno cadastrado com sucesso!" + RESET)
            input("\nPressione Enter para continuar...")
        
        elif opcao == 2:
            print("\n" + BLUE + "Cadastro de Matéria".center(60) + RESET)
            materias = get_valid_subject(materias)
            print(GREEN + "\nMatéria(s) cadastrada(s) com sucesso!" + RESET)
            input("\nPressione Enter para continuar...")
        
        elif opcao == 3:
            print("\n" + BLUE + "Cadastro de Notas".center(60) + RESET)
            print("Digite as notas do aluno abaixo:")
            notas = get_valid_grade()
            print(GREEN + "\nNotas cadastradas com sucesso!" + RESET)
            input("\nPressione Enter para continuar...")
        
        elif opcao == 4:
            print("\n" + BLUE + "Média e Classificação do Aluno".center(60) + RESET)
            if notas:
                print(class_media(notas, nome))
            else:
                print(RED + "\nNenhuma nota cadastrada. Cadastre as notas primeiro!" + RESET)
            input("\nPressione Enter para continuar...")
        
        elif opcao == 5:
            print(YELLOW + "\nSaindo do programa... Até logo!\n" + RESET)
            break
        
        else:
            print(RED + "\nOpção inválida! Escolha uma opção de 1 a 5." + RESET)
            input("\nPressione Enter para continuar...")

def get_valid_name():
    while True:
        nome = input(YELLOW + "Digite o nome do aluno: " + RESET)
        if re.search(r'\d', nome) or re.search(r'[^a-zA-Z\s]', nome):
            print(RED + "\nNome inválido! Insira um nome sem números ou caracteres especiais." + RESET)
        else:
            print(GREEN + f"\nO nome do aluno digitado foi: {nome}" + RESET)
            return nome

def get_valid_subject(materias):
    while True:
        subject = input(YELLOW + "Digite a matéria: " + RESET)
        materias.append(subject)
        print(GREEN + f"\nA matéria digitada foi: {subject}" + RESET)
        
        add_subject = input(YELLOW + "\nDeseja adicionar outra matéria? (S/N): " + RESET)
        if add_subject.lower() != "s":
            print(GREEN + "\nMatérias cadastradas: " + ', '.join(materias) + RESET)
            return materias
        else:
            print(BLUE + "\nCadastrar próxima matéria..." + RESET)

def get_valid_grade():
    notas = []
    for i in range(4):
        while True:
            nota = input(YELLOW + f"Digite a {i+1}ª nota: " + RESET)
            if re.search(r'[a-zA-Z]', nota) or re.search(r'[^a-zA-Z\s\.0-9]', nota):
                print(RED + "\nNota inválida! Insira uma nota numérica válida." + RESET)
            else:
                try:
                    valor = float(nota)
                    notas.append(valor)
                    print(GREEN + f"\nA {i+1}ª nota digitada foi: {valor}" + RESET)
                    break
                except ValueError:
                    print(RED + "\nValor inválido! Insira um número." + RESET)
    return notas

def class_media(notas, nome):
    media = sum(notas) / len(notas)
    if media >= 90:
        status = "Excelente!"
    elif 70 <= media < 90:
        status = "Bom!"
    elif 50 <= media < 70:
        status = "Regular!"
    else:
        status = "Precisa ser melhor!"
    
    resultado = (
        "\n" + "-" * 60 + "\n" +
        f"Aluno: {nome}\n" +
        f"Média: {media:.2f}\n" +
        f"Classificação: {status}\n" +
        "-" * 60 + "\n"
    )
    return resultado

# Execução principal
call_menu(nome, notas, materias)