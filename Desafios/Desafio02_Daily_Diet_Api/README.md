# DESAFIO 02 - API para controle de dieta Diária

- Nesse desafio, será desenvolvido uma API para controle de dieta diária, a Daily Diet API.

## REGRAS DA APLICAÇÃO

- Deve ser possível registrar uma refeição feita, com as seguintes informações:

  - Nome
  - Descrição
  - Data e hora
  - Está dentro ou não da dieta

- Deve ser possível editar uma refeição, podendo alterar todos os dados mencionados acima.
- Deve ser possível apagar uma refeição.
- Deve ser possível listar as refeições de um usuário.
- Deve ser possível visualizar uma única refeição.
- As informações devem ser salvas em um banco de dados.

## Requisitos iniciais

- Install [Python](https://www.python.org/)
- Install [Docker](https://www.docker.com/products/docker-desktop/)

## Instalando as dependências/bibliotecas necessárias

- Basta aplicar o seguinte comando em seu terminal:
    >
        pip3 install -r requirements.txt

## Rodando o Docker para utilizar com o Banco MySQL

- Para executar o banco de dados MySQL, ao qual foi escolhido para trabalhar neste desafio, requer o docker desktop instalado na máquina ao qual vai ser rodado o projeto.

- Em seu terminal, para executar o docker, basta aplicar os seguintes comandos:
    >
        # este comando de praste sobe o docker
        docker-compose up

        ou 

        # este comando ira subir o docker, mas sem 'travar' seu terminal com logs
        docker-compose up -d

        ou

        # este comando, caso o docker já esteja rodando, vai forcá-lo a reiniciar
        docker-compose up --force-recrease


- Após ter o docker instalando e rodando em sua máquina, precisamos criar as tabelas do nosso banco de dados e para isso, basta fazer o seguinte:

  - Inicialmente abra o terminal e insira esses comandos:
    >
        # para acessar o shell
        flask shell

        # Criando nosso banco

        # cria todas as tabelas
        db.create_all()
        # armazena todas as alterações
        db.session.commit()

        # criando usuário
        user = User(username = 'admin')
        db.session.add(user)
        db.session.commit()

        # quit flask shell
        exit()

### 🛠️ Ferramentas utilizadas no desafio:

- Flask
- Flask SQL Alchemy
- Werkzeug
- pymysql

### 📚 Conceitos utilizados no projeto:

- Criação do banco de dados.
- Criar, alterar, listar e deletar dados no banco.
- Fazer validação de requisições.
- Validar questão de chave primária e estrangeira, no momento de fazer as consultas.
