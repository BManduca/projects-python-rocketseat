# Projeto Find A Friend

## Definição do Banco de Dados

- Bando de dados [SQLite](https://www.sqlite.org/):
  - É um Banco sql
  - A mesma linguagem que geralmente temos para os outros bancos teremos aqui também no SQLite
  - Ele é considerado 'pequeno', rápido, bonito, cheio de features
  - Este banco ira simplificar e ajudar bastante durante o desenvolvimento do projeto.

## SQLAlchemy
- Python SQL Toolkit, em outras palavras é o kit de ferramentas SQL do python e Object Relational Mapper que da aos desenvolvedores de aplicativos todo o poder e flexibilidade do SQL
- O SQLAlchemy fornece um conjunto completo de padrões de persistência de nível empresarial bem conhecidos, projetados para acesso eficiente e de alto desempenho ao banco de dados, adaptados em uma linguagem de domínio simples e Pythonic.

## DBeaver
- Gerente de banco de dados
- Busca demonstrar ou ajudar a entender visualmente como que é o DB 

## Estrutura do Projeto
- Ao criar uma pasta src, dentro da mesma, já começamos a aplicar o padrão MVC, criando assim uma pasta models
  - Podemos ter uma aplicações se conectando à vários bancos, por exemplo: podemos ter uma aplicação se conectando a um sqlite e depois a um MariaDB, MySQL ou qualquer outro banco. Com base nesse conhecimento, neste projeto, estaremos utilizando o sqlite, como já visto anteriormente, desta forma, dentro de models, iremos criar uma pasta sqlite
    - Separando agora responsabilidades na integração com o banco de dados, iremos criar mais 3 pastas:
      - Settings: com o objetivos de definir conexões e afins.
      - Entities: com o objetivo de definir as entidades, ou seja, o espelhamento com o banco de dados.
      - Repositories: Serão os repositórios, ou seja, as açÕes que iremos fazer no banco.