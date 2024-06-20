# Módulo 03

- Módulo para desenvolvimento de API's com flask
- Neste módulo será abordado a questão das api's:
  - O que é uma API
  - O que é uma API rest
  - Conceito de requisições
  - Protocolo HTTP
  - Métodos

- Utilização do Python juntamente do framework Flask, para construir uma API funcional.
  - Basicamente essa API funcional será o projeto deste módulo, aonde será basicamente um crud, aonde será construído endpoints para criação, deleção, atualização e leitura.

## Flask

- O que é?
  - **Framework** leve e poderoso para construir aplicações web em python
    - Framework é um conjunto de ferramentas, bibliotecas e convençòes que fornecem uma estrutura para desenvolver aplicações.
- Vantagens:
  - Simplicidade: Uma das vantagens do Flask é a sua simplicidade e sua facilidade no aprendizado. Seu código é legível e intuitivo, tornando-o uma escolha popular para iniciantes e desenvolvedores experientes.
  - Escalabilidade: O Flask pode ser estendido com várias extensões e bibliotecas para adicionar funcionalidades conforme necessário. Isso permite escalabilidade á medida que os projetos crescem.
  - Flexibilidade: O Flask permite aos desenvolvedores escolherem suas próprias ferramentas e bibliotecas para construir aplicações personalizadas. Ele não impõe estruturas rígidas, permitindo uma abordagem mais flexível para o desenvolvimento.

- A idéia por trás do Flask era criar um Framework simples e fácil de usar, mas que também fosse poderoso e capaz de suportar o desenvolvimento de aplicações web robustas. A filosofia central do Flask foi sempre a de manter a simplicidade e fornecer aos desenvolvedores a liverdade para escolherem suas próprias ferramentas e abordagem de desenvolvimento.

- Usos conhecidos: Pinterest, LinkedIn, Netflix e Uber.

### Instalação

- pip3 install Flask, aonde podemos caso necessário passar uma versão especifica.

ou

- criando um arquivo de requisitos e instalando as dependências através do comando pip3 install -r requirements.txt

### Criando arquivo app

- inicialmene criamos o arquivo principal chamado app e nele importamos o flask e criamos uma var app, utilizamos a classe Flask, para criar passando uma varíavel geralmente como __ name __ e quando executamos de modo manual, o __ name __  recebe o valor main
    >
      from flask import Flask

      app = Flask(__name__)

### Rotas

- É como conseguimos comunicar com outros clientes, seja um usuário querendo algum tipo de informação ou usuário acessando aqui via navegador a rota
- A rota ela permite que seja criado uma comunicação, ou seja, receba informações e também devolva informações para quem está solicitando.
- É importante sempre fazer a verificação de que o name seja igual a main e apartir desta verificação, executar nosso programa, pois isto significa que estamos trabalhando localmente.

## API (Application Programming Interface)

- Basicamente a palavra chave em API, é o interface, ou seja, uma porta de entrada, uma forma de estabelecer comunicação.
- CLIENTE --REQUEST--> [ API <--> API Server ]
- O Cliente ele faz uma request para a API, que envia a requisição para o servidor da API e depois que a informação chegar, o servidor vai responder de volta para a API e assim, a mesma responde (response) para o cliente com a informação que ele espera.

  ![](./assets/FLUXO_API.png)

- API basicamente é um conjunto de regras, protocolos e ferramentas que permitem que diferentes softwares se comuniquem entre si

## API Rest (Representational State Transfer)

- Rest é um estilo de arquitetura, para o desenvolvimento de API's
- Siginifica que ele tem um conjunto de regras, que vai permitir que essa comunicação aconteça de forma fluída.
- Protocolos HTTP e/ou HTTPS
  - Operações ou Métodos:
    - GET
    - POST
    - PUT
    - DELETE
    - PATCH

- A resposta(response) no estilo REST, obrigatoriamente utilizamos o JSON ou o XML para retornar as informações.

## API vs. API Restful

- Quando uma API ela respeita todos os fundamentos do Rest, ela é nomeada como uma API Restful.
