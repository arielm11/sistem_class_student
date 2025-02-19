import re
import bd

# Códigos de cores para o terminal (ANSI escape codes)
RED    = '\033[31m'
GREEN  = '\033[32m'
YELLOW = '\033[33m'
BLUE   = '\033[34m'
CYAN   = '\033[36m'
RESET  = '\033[0m'
BOLD   = '\033[1m'

# Variáveis globais
materias = []

def print_header():
    print(BLUE + "=" * 60)
    print(BOLD + "SISTEMA DE CLASSIFICAÇÃO DE ALUNOS".center(60))
    print("=" * 60 + RESET)

def print_menu():
    print("\n" + CYAN + "Menu Principal".center(60) + RESET)
    print("-" * 60)
    print("1 - Cadastrar Matéria")
    print("2 - Listar Matérias")
    print("3 - Cadastrar Notas")
    print("4 - Listar Médias")
    print("5 - Sair")
    print("-" * 60)

def call_menu(materias):
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
            print("\n" + BLUE + "Cadastro de Matéria".center(60) + RESET)
            materias = cadastro_materia(materias)
            print(GREEN + "\nMatéria(s) cadastrada(s) com sucesso!" + RESET)
            input("\nPressione Enter para continuar...")
        
        elif opcao == 2:
            print("\n" + BLUE + "Listar Matérias".center(60) + RESET)
            listar_materia()
            input("\nPressione Enter para continuar...")
        
        elif opcao == 3:
            print("\n" + BLUE + "Cadastro de Notas".center(60) + RESET)
            cadastrar_notas()
            print(GREEN + "\nNotas cadastradas com sucesso!" + RESET)
            input("\nPressione Enter para continuar...")
        
        elif opcao == 4:
            print("\n" + BLUE + "Listar Médias".center(60) + RESET)
            media_nota()
            input("\nPressione Enter para continuar...")
        
        elif opcao == 5:
            print(YELLOW + "\nSaindo do programa... Até logo!\n" + RESET)
            break
        
        else:
            print(RED + "\nOpção inválida! Escolha uma opção de 1 a 4." + RESET)
            input("\nPressione Enter para continuar...")

def cadastro_materia(materias):
    while True:
        subject = input(YELLOW + "Digite a matéria: " + RESET)
        bd.inserir_materia(subject)
        print(GREEN + f"\nA matéria digitada foi: {subject}" + RESET)
        
        add_subject = input(YELLOW + "\nDeseja adicionar outra matéria? (S/N): " + RESET)
        if add_subject.lower() != "s":
            return materias
        else:
            print(BLUE + "\nCadastrar próxima matéria..." + RESET)

def listar_materia():
    materias = bd.listar_materias()
    if materias:
        print("\n" + BOLD + "Matérias Cadastradas:".center(60) + RESET)
        print("=" * 60)
        for id_materia, nome_materia in materias:
            print(f"ID: {id_materia} - Nome: {nome_materia}")
        print("=" * 60)
    else:
        print(RED + "Nenhuma matéria cadastrada.Cadastre uma primeiro!" + RESET)

def cadastrar_notas():
    bd.cadastrar_notas()

def media_nota():
    bd.listar_notas()

# Execução principal
if __name__ == "__main__":
    call_menu(materias)