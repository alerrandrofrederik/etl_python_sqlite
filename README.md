# etl_python_sqlite

## Desafio
criar uma pipeline de extração, limpeza, transformação e enriquecimento de dados com Python e armazenar os dados em um banco de dados SQLite de um arquivo CSV.

## Primeira etapa: job_v1.py

 no primeiro arquivo, vamos criar um novo banco de dados e uma tabela para armazenar os dados de produção de alimentos.
 obs: fi identificado que a coluna de receita total teve seu valor truncado e precisará ser corrigido.
 ![ponto para correção](https://github.com/alerrandrofrederik/etl_python_sqlite/blob/main/imagens/tabela%20ap%C3%B3s%20job1.png)

## Segunda etapa: job_v2.py
Na segunda versão do pipeline vamos carregar somente registros com quantidade produzida superior a 10 conforme a regra de negócio. Também foi restruturado o código para excluir a tabela caso já exista no banco de dados.
![Tabela filtrada]()