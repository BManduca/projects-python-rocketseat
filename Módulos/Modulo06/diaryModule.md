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
