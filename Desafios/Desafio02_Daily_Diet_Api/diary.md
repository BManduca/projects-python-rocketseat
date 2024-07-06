# Documentação do SQL Alchemy

- [Flask SQL Alchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)

## [Querying Records](https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/#)

- Recuperação dos dados no banco de dados
- Para este propósito o Flask-SQLALchemy, fornece o querycomo um atributo de consulta, em sua classe Model, que ao acessá-lo iremos receber de volta um novo objeto de consulta sobre todos os registros
- Pode ser utilizado os métodos filter() ou filter_by(), para filtrar os registros antes de disparar a seleção com all() ou first().
- Se ainda quiser usar a chave primária, pode ser usado o get().


## Documentação códigos [HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/400)

- Tópico tratando da documentação de todos os códigos HTTP para tratativas durante as requisições.
- Principais e mais utilizados:
  - 400 => { "Bad Request" }
  - 401 => { "Unauthorized" }
  - 403 => { "Forbidden" }
  - 404 => { "Not Found" }
  - 405 => { "Method Not Allowed" }
  