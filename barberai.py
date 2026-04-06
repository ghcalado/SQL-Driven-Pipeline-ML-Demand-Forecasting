import sqlite3
import pandas as pd
from datetime import datetime

DB_NAME = "barbearia.db"
CSV_OUTPUT = "dados_barbearia.csv"

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabelas():
    conn = conectar()
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT,
            data_cadastro TEXT DEFAULT (DATE('now'))
        )
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS barbeiros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ativo INTEGER DEFAULT 1
        )
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS servicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            duracao_min INTEGER NOT NULL
        )
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER REFERENCES clientes(id),
            barbeiro_id INTEGER REFERENCES barbeiros(id),
            servico_id INTEGER REFERENCES servicos(id),
            data_hora TEXT NOT NULL,
            estava_cheio INTEGER NOT NULL 
        )
    """)
    
    conn.commit()
    conn.close()

def exportar_para_orange():
    conn = conectar()
    query = "SELECT data_hora, servico_id, estava_cheio FROM agendamentos"
    df = pd.read_sql_query(query, conn)
    
    if not df.empty:
        df['data_hora'] = pd.to_datetime(df['data_hora'])
        df['dia_semana'] = df['data_hora'].dt.dayofweek
        df['hora'] = df['data_hora'].dt.hour
        
        df_final = df[['estava_cheio', 'dia_semana', 'hora', 'servico_id']]
        df_final.to_csv(CSV_OUTPUT, index=False)
    
    conn.close()

if __name__ == "__main__":
    criar_tabelas()
    exportar_para_orange()
