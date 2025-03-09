# etl_python_sqlite

## Desafio
criar uma pipeline de extração, limpeza, transformação e enriquecimento de dados com Python e armazenar os dados em um banco de dados SQLite de um arquivo CSV.

## Primeira etapa: job_v1.py

 no primeiro arquivo, vamos criar um novo banco de dados e uma tabela para armazenar os dados de produção de alimentos.
 obs: fi identificado que a coluna de receita total teve seu valor truncado e precisará ser corrigido.
 ![ponto para correção](https://github.com/alerrandrofrederik/etl_python_sqlite/blob/main/imagens/tabela%20ap%C3%B3s%20job1.png)

## Segunda etapa: job_v2.py
Na segunda versão do pipeline vamos carregar somente registros com quantidade produzida superior a 10 conforme a regra de negócio. Também foi restruturado o código para excluir a tabela caso já exista no banco de dados.
![Tabela filtrada](https://github.com/alerrandrofrederik/etl_python_sqlite/blob/main/imagens/job2.png)

## Terceira etapa: job_v3.py
Na terceira versão do pipeline vamos remover o "ponto" para evitar que o numero seja truncado.
![correção valor coluna receita total](https://github.com/alerrandrofrederik/etl_python_sqlite/blob/main/imagens/job3.png)

## Quarta etapa: job_v4.py
Na quarta versão do pipeline vamos Enriquecer a base adicionando no destino uma coluna com a margem de lucro de cada produto
obs: após criado o pipeline identificamos que a coluna de margem de lucro está com varias casas decimais e precisaremos corrigir isso.
![correção valor coluna margem de lucro](https://github.com/alerrandrofrederik/etl_python_sqlite/blob/main/imagens/job4.png)

## Quinta etapa: job_v5.py
obs: identificamos que o valor da margem de lucro tem varias casas decimais e precisaremos corrigir isso.
![correção valor coluna margem de lucro](https://github.com/alerrandrofrederik/etl_python_sqlite/blob/main/imagens/job5.png)

# Como concectar o SQLite com Power BI

### Passo 1
Baixar  e instalar o Driver do SQLite:
[Driver SQLite](http://www.ch-werner.de/sqliteodbc/)

### Passo 2
Configurar a conexão ODBC

#### 1. Abrir o ODBC:

![abrir o ODBC](https://github.com/alerrandrofrederik/etl_python_sqlite/blob/main/imagens/abrir odbc.png)

#### 2. Adicionar nova fonte:

![adicionar nova fonte](https://github.com/alerrandrofrederik/etl_python_sqlite/blob/main/imagens/adicionar_fonte.png)

![seleciona o driver](https://github.com/alerrandrofrederik/etl_python_sqlite/blob/main/imagens/seleciona o driver.png)

![configurar o driver](https://github.com/alerrandrofrederik/etl_python_sqlite/blob/main/imagens/configuracao.png)

![conectar ao banco de dados](https://github.com/alerrandrofrederik/etl_python_sqlite/blob/main/imagens/selecao_DB.png)

### Passo 3
Conectar ao banco de dados no Power BI comm conexão ODBC

![conectar ao PBI](https://github.com/alerrandrofrederik/etl_python_sqlite/blob/main/imagens/conexao_PBI.png)