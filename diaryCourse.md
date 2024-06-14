# O que é Python?

- É uma linguagem orientada a objetos
- De tipagem dinâmica e forte
- Interativa e interpretada

- O python em si é uma linguagem bem popular

## Linguagem de alto nível

- Basicamente a linguagem de alto nível, é uma linaguagem que se assemelha muito mais a linguagem humana do que a linguagem das máquinas

## O Python por 'debaixo dos panos'

- O Python é interpretado por byte code pelo interpretador do python, tornando possível o codígo ser portável, ou seja,isso quer dizer que podemos compilar o nosso código em uma plataforma e executar em outras plataformas
  - Plataformas: Linux, Windows, Mac...
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

&nbsp;

## Estrutura de dados

### Listas

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

#### Métodos em listas

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

&nbsp;

### Tuplas

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

#### Métodos em tuplas

- Count()
  - Retonar a quantidade de vezes que um elemento aparece na tupla
        >
            minha_tupla = (1, 2, 3, 4, 4, 5)
            contagem = minha_tupla.count(4)
            print('Quantidade de vezes que o elemento 4 aparece: ', contagem)

- Index()
  - retorna o índice do elemento que procuramos

&nbsp;

### Dicionários

- Coleção não ordenda, de pares chave/valor.
- Dicionários náo são ordenados como nas listas e tuplas.

&nbsp;

#### Métodos em dicionários

- Para remoção de um objeto [chave: valor], podemos utilizar o del

    >
        del pessoa['sobrenome']

- Keys()
  - retorna todas as chaves do nosso dicionário em formato de lista

- values()
  - Retorna todos os valores do meu dicionário em formato de lista

- items()
  - Retorna uma lista de tuplas, contendo todos os pares chave-valor do meu dicionário

&nbsp;

## Condicionais

- Permitem tomar decisões com base em condições e essa decisões irão executar um bloco de código,  
que vai estar dentro desta condicional

&nbsp;

## Entrada de dados

- opção do usuário inserir informações em tempo real de execução de um programa.

### Função input

- função utilizada para inserção de informações ou dados em uma varíavel, por exemplo

&nbsp;

## Loops

- É uma estrutura que permite repetir um bloco de código enquanto uma condição for verdadeira
- São utilizados para automatizar tarefas repetitivas e executar ações repetidas vezes
- Existem dois tipos de loops: For e While

### Loop For
    >
        lista = [1, 2, 3, 4, 5, 6]

        print('\nLISTA')
        for element in lista:
            print(f'{element}')

        print('\nTUPLA')
        tupla = (1, 2, 3, 4, 5, 6)
        for element in tupla:
            print(f'{element}')

        print('\nDICIONÁRIO')
        pessoa = {'nome': 'Brunno', 'sobrenome': 'Manduca', 'idade': 32, 'cidade': 'Florianópolis'}

        print('\nUSO DO FOR APRESENTANDO AS CHAVES DE UM DICIONÁRIO')
        for key in pessoa.keys():
            print(f'{key}')

        print('\nUSO DO FOR APRESENTANDO OS VALORES DE UM DICIONÁRIO')
        for element in pessoa.values():
            print(f'{element}')

        print('\nUSO DO FOR APRESENTANDO A CHAVE-VALOR DE UM DICIONÁRIO')
        for key, element in pessoa.items():
            print(f'{key} => {element}')

#### Função range()

- retorna um intervalo numérico em formato de lista
- imprimindo valores do 0 ao 9, com uso do range
    >
        for i in range(0,10):
            print(i)

- caso eu quisesse fazer o print dos valores de 0 ao 4, poderia fazer de duas formas:
    >
        for i in range(0,5):
            print(i)

  OU

- automaticamente já inicia no valor 0
    >
        for i in range(5):
            print(i)

- podemos utilizar juntamente com o range, a função len(), ao qual verifica o tamanho do objeto que esta sendo analisado e também fazer uma manipulação de uma lista:
    >
        print('\nUSO DA FUNÇÃO RANGE() COM LEN()')
        for element in range(0, len(lista)):
            print(f'Elemento {element} => {lista[element]}')

    >
        lista = [1, 2, 3, 4, 5, 6]
        for element in range(0, len(lista)):
            if element == 3:
                lista[element] = 5
            else:
                lista[element] = 0
            print(f'Elemento {element} => {lista[element]}')

#### Função enumerate()

- é uma função poderosa que facilita a tarefa de percorrer uma lista enquanto acompanha os índices de cada elemento

&nbsp;

### Loop While

- Tipo de loop utilizado para repetir um bloco de código, enquanto uma condição for verdadeira.

- Utilização do break
  - serve para forçar a parada do laço diante de alguma situação apresentada dentro do laço.
  - pode ser utilizado tanto no for quanto no while.

&nbsp;

## Funções no Python

- Funções é um bloco de código reutilizado, ou seja, um bloco que é possível reutilizar várias vezes e o mesmo executa uma tarefa específica quando é acionado.

&nbsp;

## Exceções

- São eventos que ocorrem durante a execução do código e podem interromper o programa, se não tratar as mesmas adequadamente.

### raise

- Permite que o código seja interrompido propositalmente

&nbsp;

## Módulos

- São arquivos que contém definições e instruções que podem ser reutilizadas por outros programas.

- Existem duas formas de realizar importação de módulos (as duas tem o mesmo efeito)

1. import
    >
        import math

        raiz_quadrada = math.sqrt(25)
        print(f'A raiz quadrada de 25 é: {raiz_quadrada}')

2. from
    - aonde nesta forma, iremos importar somente o que estamos utilizando e isto é uma boa prática.

    >
        from math import sqrt

        raiz_quadrada = sqrt(25)
        print(f'A raiz quadrada de 25 é: {raiz_quadrada}')

&nbsp;

## Módulos de terceiros

- iremos utilizar o gerenciamento de pacote pip, para realizar a instalação desses pacotes(módulos)

1. Biblioteca requests

- é uma bilbioteca que contém uma série de instruções e funções que nos ajudam a fazer requisições http, basicamente requisições em sites da internet
- instalação: pip3 install requests | para uma versão especifica, podemos rodar o seguinte comando pip3 install requests==2.31.0

&nbsp;

## POO

- Programação orientada a objetos, basicamente é uma linguagem que adota e implementa os príncipios e conceitos da programação orientada a objetos.
- Paradigma de programação, que se baseia na organização dos programas em torno de objetos.
- Objetos: São instâncias de classes.

- Exemplos: Python, Javam, C++, C#, Ruby, essas linguagens oferecem suporte nativo a programação orientada a objetos.
- Permite que os programadores criem softwares de forma modular, reutilizavel e mais fácil de se entender e manter, seguindo os príncipios e os conceitos da POO.
- No paradigma orientado a objetos, temos que pensar diretamente em classe e objetos. Ela foi criada em si, para trazer mais para nossa realidade, nossa estrutura de visualização, essa forma como enxergamos o mundo, para dentro da programação.

- Vantagens:
  - Por exemplo ao criarmos uma conta bancária, nós já temos, uma estrutura definida, que seria uma classe e através da classe, nós já temos os métodos que são permitidos e deta forma, não precisamos recriar tudo do zero, sendo assim, podemos reutilizar o código.
  - organização e estrutura, não precisamos ficar olhando as intâncias do objeto para saber o que ele pode fazer, pois, podemos ir direto na classe e conseguimos olhar os atríbutos e os métodos, que são utilizados.

&nbsp;

### Classes

- São modelos, um plano que define a estrutura e o comportamento desses objetos

### Objetos

- É uma instância da classe criada
- São criados apartir da classe definida e respeita os atributos e métodos que a classe tem.
- Podem representar entidades do mundo real(ex.: carros, pessoas, contas bancárias, plantas...)

### Atríbutos

- São os dados dessa classe/estrutura que estamos criando

### Métodos

- São as funções que a classe pode ter

### Desvantagens POO

- Complexidade: para aplicações simples, é aplicado uma carga de complexidade não necessária, porém, ao mesmo tempo o programador terá ujma organização muito melhor, uma reutilização do código, uma proteção das suas propriedades, será possível reutilizar as classes através da herança, vai conseguir abstrair código..

- Curva de aprendizado: POO é prática basicamente, ou seja, não é algo que se aprende do dia para a noite, requer experiência, requer uma forma diferente de enxergar o mundo.


### Pilares de POO

#### Encapsulamento

- Basicamente é uma técnica poderosa que permite controlar o acesso aos atributos e métodos de uma classe
- Uso de atríbutos privados, para justamente proteger a informação, proteger o dado de ser manipulado de maneira errônea durante a execução do programa.
- funciona com a utilização de modificadores de acesso para restringir o acesso aos atributos e aos métodos de um objeto
- para transformar um atríbuto em privado, basta fazermos o seguinte: adicionar '__' antes do mesmo.
    >
        class ContaBancaria:
            def __init__(self, saldo) -> None:
                self.__saldo = saldo # atributo privado

#### Herança

- é um princípio da POO que permite a uma classe derivar propriedades e métodos de outra classe

#### Polimorfismo

- Nos ajuda na reutilização de um método definido na classe mãe, so que re-implementado de uma forma diferente

#### Abstração

- 