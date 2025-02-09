import re

'''Definir funções'''
'''Função para validar o nome'''
def get_valid_name():    
    while True:
        nome = input("Digite o nome do aluno: ")

        if re.search(r'\d', nome) or re.search(r'[^a-zA-Z\s]', nome):
            print("Nome inválido! Inserir um nome sem números e caracteres especiais.")  
        else:  
            print(f"O nome do aluno digitado foi: {nome}")
            return nome

'''Função para validar as notas'''
def get_valid_grade():

    notas = []
    for i in range(4):
        while True:
            nota = input(f"Digite a {i+1}ª nota: ")
            if re.search(r'[a-zA-Z]', nota) or re.search(r'[^a-zA-Z\s\.0-9]',nota):
                print("Nota inválida! Inserir uma nota sem letras ou caracteres especiais.")
            else:
                print(f"A {i+1}ª nota digitada foi: {nota}")
                notas.append(float(nota))
                break
    return notas

'''Função para classificar a média'''
def class_media(media):
    if media >= 90:
        return "Excelente!"
    elif 70 <= media < 90:
        return "Bom!"
    elif 50 <= media < 70:
        return "Regular!"
    else:
        return "Precisa ser melhor!"
            
'''Execução principal'''
nome = get_valid_name()
notas = get_valid_grade()
media = sum(notas) / len(notas)

print(f"A média do aluno {nome} foi: {media}.\n{class_media(media)}")