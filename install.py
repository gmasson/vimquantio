#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('database.db')
database = conn.cursor()

# Criando a tabela (Dados Minerados)
database.execute("""
CREATE TABLE mining (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        url TEXT NOT NULL,
        title TEXT NOT NULL,
        text TEXT NOT NULL,
        date_verification TEXT NOT NULL
);
""")

conn.commit()

# Criando a tabela (Cache)
database.execute("""
CREATE TABLE cache (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        url TEXT NOT NULL,
        html TEXT NOT NULL
);
""")

conn.commit()

print('Tabelas criadas com sucesso.')

# Desconectando...
conn.close()
