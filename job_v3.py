# Criação de Pipeline de Extração, Limpeza, Transformação e Enriquecimento de Dados
# Versão 3
# Na terceira versão do pipeline vamos remover o "ponto" para evitar que o numero seja truncado.

# Importação de Bibliotecas
import pandas as pd
import sqlite3
import csv

# Função que substiui o ponto por vazio da ultima coluna
def remove_ponto(value):
    return int(value.replace('.', ''))

# Abre o arquivo CSV com os dados de produção de alimentos
with open('producao_alimentos.csv', 'r') as file:
    
    # Cria um leitor de CSV para ler o arquivo
    reader = csv.reader(file)

    # Pula a primeira linha, que contém os cabeçalhos das colunas
    next(reader)

    # Conecta ao banco de dados
    conn = sqlite3.connect('dados.db')

    # Deleta a tabela existente, se houver
    conn.execute('DROP TABLE IF EXISTS producao')

    # Criar uma tabela para armazenar os dados de produção de alimentos
    conn.execute('''
        CREATE TABLE producao (
            produto TEXT,
            quantidade INTEGER,
            preco_medio REAL,
            receita_total REAL
        )
    ''')

    # insere cada linha do arquivo com quantidade maior que 10 na tabela do banco de dados
    for row in reader:
        if int(row[1]) > 10:

            # Remove o ponto do valor da última coluna e converte para inteiro
            row[3] = remove_ponto(row[3])

            # Insere a linha na tabela do banco de dados
            conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) VALUES (?, ?, ?, ?)', row)
    # Grava e fecha a conexão
    conn.commit()    
    conn.close()

print('Job concluído com sucesso!')