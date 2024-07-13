# Módulo 05 - Notificações em tempo real

- Neste módulo, o foco será de explorar o conceito de notificações em tempo real e suas aplicações, além de discutir as estratégias mais comuns para implementá-las, como long polling e WebSockets.

## Notificações em tempo real

- Basicamente um sistema que implementa notificações em tempo real, ele tem a capacidade de enviar informações imediatas e também informações(dados) em tempo real para os clientes conectados a uma aplicação web.

- Esses clientes(usuários) que estão conectados vão receber as notificações sem precisar, ficar atualizando a página a todo momento.

- Porque é útil?
  - Porque fornece atualizações instantâneas aos usuários sem que eles tenha que atualizar manualmente a página.

- Tecnologia WebSockets
  - Um protocolo de comunicação bidirecional, ou seja, que permite que os dois lados, o cliente e o servidor se comuniquem entre si, através de uma comunicação eficiente e em tempo real.

    ![](./assets/WebSockets_ilustration.png)

  - Latência é a mínima possível
    - latência é tempo que demora para a informação 'ir e voltar'.

  - Exemplos de aplicações
    - Aplicações de Chat em tempo real
    - Rastreamento de Atividades
    - Colaboração em tempo real

## Long polling vs. WebSockets
![](./assets/long_polling_vs_websockets.png)

1. Long polling

   - A requisição vem do client para o servidor, toda vez que preciso dessa informação atualizada
   - Exemplo: Toda vez que preciso ver meu saldo atualizado em uma aplicação, eu precisaria clicar em um botão e no momento que o botão é clicado, uma requisição vai no servidor e o sevidor vai processar essa informação e devolve a mesma atualizada

   - No LP há um grande overhead na rede, pois toda vez estamos abrindo/enviando conexões  ou requisições para o sevidor e o servidor processa e envia a informação para o client
   - Essa ação tem um custo de rede, de dado tráfegado (grandes clouds), tem custo de processamento.

2. WebSockets

   - É efetuado uma única o vez o Hand shake, ou seja, assim que a conexão for estabelecida, o servidor consegue enviar várias informações para o client, da mesma forma que o client consegue enviar para o sevidor.

3. Conclusão

   - O uso do WebSockets proporciona uma experiência mais fluida e eficiente em notificações em tempo real
  