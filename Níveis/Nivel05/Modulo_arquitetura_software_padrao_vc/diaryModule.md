# Arquitetura de Software e Padrão MVC

![](./assets/padrao_mvc.png)

## Introdução ao Padrão MVC

- O Padrão MVC (Model-View-Controller) foi introduzido por um engenheiro norueguês em 1978 e é amplamente utilizado na organização de código de sistemas que envolvem interface do usuário e lógica de negócio. O padrão separa as responsabilidades em três componentes principais: model, view e controller. A view lida com a interface de usuário, o controller processa as entradas do usuário e utiliza o model conforme necessário e o model gerencia os dados do aplicativo. O MVC é comum em diversas linguagens e frameworks como Django, Spring Boot e Laravel.

## Responsabilidades do Padrão MVC

![](./assets/explanation_mvc.png)

- Views
  - A view é responsável por apresentar os dados de resposta e por lidar com a interface de interação com o usuário.

- Controllers
  - O Controller recebe as entradas do usuário da View, processa essas entradas e atualiza o Model conforme necessário. O Controller armazena a regra de negócio do sistema.

- Model
  - O Model é responsável por armazenar e gerenciar os dados do aplicativo, bem como fornecer métodos para acessar e manipular esses dados.
  - Camada para interagir com banco de dados, para armazenar elementos que serão importantes para a aplicação e para quem está desenvolvendo, obtendo assim essa persistência de dados.
  - O Model, pode ter também uma lógica para armazenamento em diversos outros locais, como por exemplo: CSV, arquivos de texto.

## Ambientes Virtuais

- Sempre existe aquela questão de executar um projeto e logo em seguida outro desenvolvedor ou colega de equipe, vai tentar executar o mesmo projeto e acaba resultando em algo insperado e não roda o projeto e isso acontece justamente por serem máquinas diferentes, com versões diferentes e até mesmo OS diferentes, desta forma, para que isso não venha ocorrer, podemos utilizar os ambientes virtuais.
- Estaremos utilizando aqui neste módulo o Virtualenv, que o próprio python nos oferece.
- instalação: mas para instalar unicamente o virtualenv, basta digitar pip3 install virtualenv
- para inicializar e criar o ambiente virtual => python3 -m venv venv e logo em seguida, podemos ver dentro do projeto uma pasta denominada venv
- Ativando o ambiente virtual => source nome_do_diretorio/bin/activate
  - no meu caso, ficaria source venv/bin/activate
- Desativando o ambiente virtual => basta digitar deactivate
- Para armazenar todas as libs e versões que estou utilizando no meu ambiente virtual
  - venv/bin/pip3 freeze > requirements.txt

## Pylint
- Ele busca analisar erros, impõe um padrão de codificação, procura por code smells e pode fazer sugestões sobre como o código pode ser refatorado.
  - code smells: São características no código-fonte de um programa que podem indicar um problema mais profundo. Eles podem ser um sinal de que as boas práticas de design não foram aplicadas, mas não necessariamente um bug no sistema.
- Para separar todas as regrar que o pylint possui, iremos aplicar o seguinte comando: pylint --generate-rcfile > .pylintrc