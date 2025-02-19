import psycopg2
import re

# Códigos de cores para o terminal (ANSI escape codes)
RED    = '\033[31m'
GREEN  = '\033[32m'
YELLOW = '\033[33m'
BLUE   = '\033[34m'
CYAN   = '\033[36m'
RESET  = '\033[0m'
BOLD   = '\033[1m'

# Configuração do banco de dados
DB_CONFIG = {
    "dbname": "atosprd",
    "user": "postgres",
    "password": "8813",
    "host": "localhost",  # ou o IP do servidor PostgreSQL
    "port": "5432"  # Porta padrão do PostgreSQL
}

# Criando conexão
try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    print("Conexão bem-sucedida!")

    # Criar tabelas se não existirem
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS materia (
        ID_MATERIA SERIAL PRIMARY KEY,
        NOM_MATERIA TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS nota (
        NOTA_ID SERIAL PRIMARY KEY,
        ID_MATERIA INTEGER NOT NULL, 
        NOTA_1 REAL NOT NULL CHECK (NOTA_1 >= 0 AND NOTA_1 <= 100),
        NOTA_2 REAL NOT NULL CHECK (NOTA_2 >= 0 AND NOTA_2 <= 100),
        NOTA_3 REAL NOT NULL CHECK (NOTA_3 >= 0 AND NOTA_3 <= 100),
        MEDIA REAL NOT NULL CHECK (MEDIA >= 0 AND MEDIA <= 100),
        FOREIGN KEY (ID_MATERIA) REFERENCES materia(ID_MATERIA) ON DELETE CASCADE
    );
    """)

    conn.commit()  # Salvar as mudanças
    print("Tabelas criadas com sucesso!")

except Exception as e:
    print(f"Erro ao conectar ao PostgreSQL: {e}")

finally:
    if 'conn' in locals():
        cursor.close()
        conn.close()
        print("Conexão encerrada.")     
        
def inserir_materia(nome_materia):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO materia (NOM_MATERIA) VALUES (%s) RETURNING ID_MATERIA;", (nome_materia,))
        #id_materia = cursor.fetchone()[0]  Obtém o ID gerado
        
        conn.commit()
        print(f"Matéria '{nome_materia}' inserida!")
    
    except Exception as e:
        print(f"Erro ao inserir matéria: {e}")
    
    finally:
        cursor.close()
        conn.close()

def listar_materias():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        cursor.execute("SELECT id_materia,nom_materia FROM materia;")
        materias = cursor.fetchall()
        return materias
        
    except Exception as e:
        print(f"Erro ao listar matérias: {e}")
    
    finally:
        cursor.close()
        conn.close()
        
def cadastrar_notas():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        cursor.execute("SELECT id_materia,nom_materia FROM materia;")
        materias = cursor.fetchall()
        print("\n" + BOLD + "Matérias Cadastradas:".center(60) + RESET)
        print("=" * 60)
        for id_materia, nome_materia in materias:
            print(f"ID: {id_materia} - Nome: {nome_materia}")
        print("=" * 60)

        materia_id = input(YELLOW + "\nDigite o ID da materia: " + RESET)
        cursor.execute("SELECT nom_materia FROM materia WHERE id_materia = %s;", (materia_id,))
        nome_materia = cursor.fetchone()
        
        print(f"Matéria '{nome_materia}' selecionada!")
        
        notas = []
        for i in range(3):
            while True:
                nota = input(YELLOW + f"Digite a {i+1}ª nota: " + RESET)
                if re.search(r'[a-zA-Z]', nota) or re.search(r'[^a-zA-Z\s\.0-9]', nota):
                    print(RED + "\nNota inválida! Insira uma nota numérica valida." + RESET)
                else:
                    try:
                        valor = float(nota)
                        notas.append(valor)
                        print(GREEN + f"\nA {i+1}ª nota digitada foi: {valor}" + RESET)
                        break
                    except ValueError:
                        print(RED + "\nValor inválido! Insira um número." + RESET)
        
        cursor.execute("INSERT INTO nota (ID_MATERIA, NOTA_1, NOTA_2, NOTA_3, MEDIA) VALUES (%s, %s, %s, %s,%s);", (materia_id, notas[0], notas[1], notas[2], (notas[0] + notas[1] + notas[2]) / 3))
        conn.commit()
    
    except Exception as e:
        print(f"Erro ao inserir matéria: {e}")
    
    finally:
        cursor.close()
        conn.close()
    
def listar_notas():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute("SELECT m.nom_materia, n.nota_1, n.nota_2, n.nota_3, n.media FROM materia m INNER JOIN nota n ON m.id_materia = n.id_materia;")
        materias = cursor.fetchall()
        if materias:
            print("\n" + BOLD + "Notas Cadastradas:".center(60) + RESET)
            print("=" * 60)
            for materia, nota1, nota2, nota3, media in materias:
                print(f"Matéria: {materia} - Nota 1: {nota1} - Nota 2: {nota2} - Nota 3: {nota3} - Média: {media}")
            print("=" * 60)
        else:
            print(RED + "\nNenhuma matéria cadastrada. Cadastre uma matéria primeiro!" + RESET)
    
    except Exception as e:
        print(f"Erro ao inserir matéria: {e}")
    
    finally:
        cursor.close()
        conn.close()