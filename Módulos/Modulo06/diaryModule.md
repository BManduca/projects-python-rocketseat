# Módulo 06 - Introdução ao design de código

## Typing

- Basicamente é um meio para indicar os tipos esperados para os elementos de entrada e o tipo de retorno da função.

## Method public vs. Mehotd private

- Método privado ele não pode ser acessado de fora da minha classe declarada, ou seja, um objeto não pode chamar o método privado, entretanto, dentro do contexto da minha classe, podemos através de um outro método acessar o método privado
- Mas para que isso serve?
  - Basicamente métodos privados servem para quando buscamos proteger lógicas internas da própria classe e informações sensíveis.
  - Ao tornar um método privado, ele só pode ser acessado por dentro da classe, o que garante a segurança dos dados.
  - Sem dizer que o código fica mais elegante e de fácil manutenção.

## Ferramentas usadas no projeto

- Blueprint
  - Para trabalhar com projetos maiores torna-se necessário modularizar a aplicação, separando assim as responsabilidades em arquivos diferentes.
  - No Flask, esse conceito é chamado Blueprints
  - Blueprints são aplicações em Flask que se acoplam em uma aplicação principal.


## Testes unitários

- A idéia em si é criar funções de testes que verifiquem o comportamento
correto de partes específicas do projeto.
- Uso da palavra 'assert' -> Comando ou palavra reservada no python em que vai ser testado a veracidade do que foi implementado logo a frente.
- Aqui para os testes que estaremos trabalhando, podemos utilizar um elemento controlado para trabalho, que chamamos de Mock e dentro do arquivo de teste, criamos uma classe da seguinte forma:
    >
      class MockRequest:
        def __init__(self, body: Dict) -> None:
            self.json = body
  - Aonde passamos o body (Dict) como parâmetro e fazemos o self.json, receber o body
- Logo em seguida, dentro da função de test_calculate, que criamos, definimos um mock_request, ao qual vai receber a chamada da class que criamos, passando o body, com um valor number definido, simplesmente neste primeiro momento para teste
    >
      mock_request = MockRequest(body={
          'number': 1
      })
- Basicamente os testes unitários eles vem para ajudar a ter uma qualidade de código, pois, para qualquer alteração por mais mínima que seja, ira passar pelos testes e caso tenha divergência(s) será barrado, gerando assim uma análise por parte de quem estará realizando a execução.