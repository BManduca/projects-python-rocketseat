# Projeto Sample Flask Auth

- Antes de iniciar, é importante entender o papel do banco de dados na persistência das informações. Em alguns projetos que eu desenvolvi, muitos dados foram armazenados em estruturas de dados do Python, como listas e dicionários. Isso ocorre porque essas dados são armazenados na memória RAM, que é volátil e não persiste os dados. Para contornar essa situação, foi utilizado o banco de dados, que é uma ferramenta para persistir informações.

- Existem diferentes tipos de Banco de Dados:
  - MySQL
  - PostgreSQL
  - SQLite
  - MongoDB
  - Amazon Aurora
  - Amazon DynamoDB

- Durante o projeto, estarei utilizando o SQL Alchemy, que é uma extensão do Flask que suporta o SQL ALchemy.
  - O SQL Alchemy é um ORM (Object Relational Mapper), que permite abstrair as funções do banco de dados e facilita a troca de banco de dados no futuro.

- O Flask SQL Alchemy não é um **Banco de Dados**. Ele é apenas uma ferramenta ORM que ajuda a conectar e realizar as interações dentro do projeto.

- Durante o projeto, foi orientado a utilização do SQLite, que é uma ótima opção para projetos de desenvolvimento, segundo o Professor, pois é leve e fácil de usar. No entanto, não é adequado para aplicação em produção, devido as limitações de gerenciamento de requisições concorrentes.