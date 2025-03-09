# Criação de Pipeline de Extração, Limpeza, Transformação e Enriquecimento de Dados
# Versão 1

# Importação de Bibliotecas
import pandas as pd
import sqlite3
import csv

# Criar um novo banco de dados
conn = sqlite3.connect('dados.db')

# Criar uma tabela para armazenar os dados de produção de alimentos
conn.execute('''
    CREATE TABLE producao (
        produto TEXT,
        quantidade INTEGER,
        preco_medio REAL,
        receita_total REAL
    )
''')

# Grava e fecha a conexão
conn.commit()
conn.close()

# Abre o arquivo CSV com os dados de produção de alimentos
with open('producao_alimentos.csv', 'r') as file:
    
    # Cria um leitor de CSV para ler o arquivo
    reader = csv.reader(file)

    # Pula a primeira linha, que contém os cabeçalhos das colunas
    next(reader)

    # Conecta ao banco de dados
    conn = sqlite3.connect('dados.db')

    #insere cada linha do arquivo CSV na tabela producao
    for row in reader:
        conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) VALUES (?, ?, ?, ?)', row)

    # Grava e fecha a conexão
    conn.commit()    
    conn.close()

print('Dados carregados com sucesso!')