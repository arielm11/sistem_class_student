import psycopg2

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
        
