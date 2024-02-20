
import sqlite3

DATABASE = 'database.db'

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        print("Conexão ao banco de dados SQLite bem-sucedida.")
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados SQLite: {e}")
    return conn

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Tbs (
                id INTEGER PRIMARY KEY,
                quantidade int NOT NULL,
                nome TEXT NOT NULL,
                telefone int NOT NULL
            )
        ''')
        print("Tabela criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela: {e}")
