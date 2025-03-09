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