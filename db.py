import sqlite3
import time

conn = sqlite3.connect('UserData.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    Usuario TEXT NOT NULL,
    Senha TEXT NOT NULL
);
""")

print("Conectando ao Banco de Dados...")
time.sleep(1)
print("Conectado com sucesso!")