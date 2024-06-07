# O que é Python?
- É uma linguagem orientada a objetos
- De tipagem dinâmica e forte
- Interativa e interpretada

- O python em si é uma linguagem bem popular

## Linguagem de alto nível
- Basicamente a linguagem de alto nível, é uma linaguagem que se assemelha muito mais a linguagem humana do que a linguagem das máquinas

## O Python por 'debaixo dos panos'
- O Python é interpretado por byte code pelo interpretador do python, tornando possível o codígo ser portável, ou seja,isso quer dizer que podemos compilar o nosso código em uma plataforma e executar em outras plataformas
    * Plataformas: Linux, Windows, Mac...
- A especificação do Python é mantida por uma instituição chamada O Python Foundation Software e a sua versão oficial é escrita em C e é por isso que podemos encontrar muitas referências por C-Python também.
- Além de ser muito utilizado no desenvolvimento de software, o Python também é utilizado para outras atividades, como:
    1. Automação de tarefas e até extensão de funcionalidades em outras ferramentas, como por exemplo, o Excel.

## Variáveis
- Na parte de declaração, existem duas formas de efetuar a criação ou declaração de variáveis:
    - snake_case
        - nome_completo = 'Brunno Manduca'

    - camelCase
        - nomeCompleto = 'Brunno Manduca'


- Em python existe a predefinição que para classes utilizamos o camelCase e para variáveis, funções e métodos utilizamos o snake_case

## Type
- Em algum momento se precisarmos verificar o tipo que estamos trabalhando ou somente querer identificar o tipo da váriavel, podemos aplicar o comando type, da seguinte forma:
    >
        numero_real = 3.14
        print(f'A valor {numero_real} é do tipo {type(numero_real)}')

    - Assim, será mostrado o valor presente na váriavel e o tipo da mesma


## Upper e Lower case
- Uppercase é o método que utilizamos quando precisamos que um texto ou uma única palavra esteja todo em 'caixa alta', exemplo: BRUNNO
    >
        print('Nome completo utilizando método Uppercase => {}'.format(nome_completo.upper()))

- Lowercase é o método que utilizamos quando precisamos que um texto ou uma única palavra esteja todo em 'caixa baixa', exemplo: brunno
    >
        print('Nome completo utilizando método Lowercase => {}'.format(nome_completo.lower()))

## Método Count
- O método count(), de maneira geral, o count serve para diagnosticar quantas vezes aparece uma ocorrência baseada em um parâmetro, ao qual é passado na chamada do método, por exemplo, quantas vezes tem a ocorrência de uma letra dentro de uma palavra.

    >
        nome = 'Brunno'
        print(nome.count('n'))

## Método find()
- O método find(), é uma função usada para encontrar o índice da primeira ocorrência de uma substring dentro de uma determinada string.

## Método encode()
- Método para realizar a codificação de um texto em bytes, por exemplo.

## Método decode()
- Método para realizar a decoficação de um texto que já se encontra em bytes, para voltar a ser um texto, sem estar codificado.

## Método replace()
- método para realizar a substituição de uma string por outra.
    >
        nome_completo = 'Brunno'
        nome_completo.replace("o","a")

## Método Join()
- Método para adicionar um separado a cada caractere que temos na string.

## Método split()
- Método que irá dividir a string em uma lista, com base em um caracter alvo que for passado para o método, como default, o método já entende o espaço como um separador.

    >
        nome_completo = 'Brunno Manduca'
        nome_completo.split()

## Método strip()
- Método para remover caracteres indesejados ou espaços no ínicio e no fim de uma string
- se caso desejar remover um elemento que esteja somente a direita da string, podemos utilizar o método rstrip()

## Método startswith()
- Método para analisar e retornar se determinada string inicia com o padrão passado como parâmetro

    >
        nome_completo = 'Brunno'
        nome_completo.startswith('Br')

## in e not in
- in é para quando precisamos saber se existe uma ocorrência do valor passando como parâmetro dentro da varíavel que eu estou analisando

- not in é para quando precisamos saber se não existe uma ocorrência do valor passando como parâmetro dentro da varíavel que eu estou analisando

## Operadores lógicos
- and: Sempre vai validar se as duas entradas passadas forem verdadeiras.
    1. True and True => True
    2. True and False => False
    3. False and False => False

- or: Sempre vai validar se uma das duas entradas passadas é verdadeira.
    1. True or False => True
    2. False or False => False


## Listas
- Coleção de elementos ordenáveis e mutáveis

- Fatiamento de listas (slice)

    >
        minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(minha_lista[1:9])

- Para 'fatiar' do começo ate a posição desejada, podemos fazer da seguinte forma:

    >
        minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(minha_lista[:8])

- Para 'fatiar' de um elemento desejado ate o final da lista, podemos fazer da seguinte forma:

    >
        minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(minha_lista[2:])


### Métodos em listas

- Append()
    - Adiciona um elemento ao final da lista

- Index()
    - retorna o índice do elemento que procuramos

- Insert()
    - Insere um elemento em um index específico

- Pop()
    - Método que remove e retorna o índice de um item específico
    - o valor de index padrão do pop é -1, desta forma, sempre temos que passar um valor mais de index ao qual queremos remover

- Remove()
    - Método que remove o primeiro elemento com o valor especificado

- Sort()
    - organiza a lista de maneira crescente

## Tuplas
- Coleção ordenada e imutável

- Para acessar os elementos é igual ao da lista, passando a posição desejada
    >
        minha_tupla = (1, 2, 3, 4, 4, 5)
        print(minha_tupla[0])
        print(minha_tupla[2])

- Nas tuplas, caso precise mostrar ou acessar o último elemento, passamos com index negativo
    >
        minha_tupla = (1, 2, 3, 4, 4, 5)
        print(minha_tupla[-1])

### Métodos em tuplas

- Count()
    - Retonar a quantidade de vezes que um elemento aparece na tupla
        >
            minha_tupla = (1, 2, 3, 4, 4, 5)
            contagem = minha_tupla.count(4)
            print('Quantidade de vezes que o elemento 4 aparece: ', contagem)

- Index()
    - retorna o índice do elemento que procuramos
