'''
    \033[m => contra barra + 033 + abrir colchetes e fechar o código com a letra "m"

    \033[ m
    E entre esse colchetes e "m" você vai colocar o código da cor.
    Você poderá colocar 0 código, 1 código, 2 ou 3 códigos.
    ex: com 3 códigos
    \033[0;33;44m

    Primeiro código "0" que eu inseri foi do "comportamento", 
    "STYLE" (Negrito, normal, itálico, Sublinhada )

    Em seguida você colocará o " ; " (para separar ).

    Segundo código "33" é o código do "Texto", "TEXT" (cor do texto )
    
    Terceiro código "44" é o código de "cor de fundo" , "BACKground" (cor do fundo)

    ALGUNS CODIGOS PARA STYLE SÃO:
    0 = None (sem estilo)
    *esse primeiro código é opcional caso você queria deixar sua fonte normal, 
    pode colocar ou não o "0", deixando v.
    1 = Bolde (Negrito)
    2 = Fraco
    3 = Itálico
    4 = Underline (Sublinhado)
    7 = Negative (Inverter as configurações Fundo vai pra letra e letra fundo)

    ALGUNS CODIGOS PARA TEXT SÃO (30 a 37):
    30 = Branco
    31 = Vermelho
    32 = Verde
    33 = Amarelo
    34 = Azul
    35 = Magenta
    36 = Ciano (*imagine ciano aqui, não tem pra por no texto ^.^')
    37 = Cinza

    ALGUNS CODIGOS PARA BACK SÃO (40 a 47):
    40 = Branco
    41 = Vermelho
    42 = Verde
    43 = Amarelo
    44 = Azul
    45 = Magenta
    46 = Ciano
    47 = Cinza
'''

colors = (
    '\033[0m', # 0 - SEM COR
    '\033[0;30m', # 1 - BRANCO
    '\033[0;31m', # 2 - VERMELHO
    '\033[0;32m', # 3 - VERDE
    '\033[0;33m', # 4 - AMARELO
    '\033[0;34m', # 5 - AZUL
    '\033[0;35m', # 6 - ROXO
    '\033[0;36m', # 7 - CIANO
    '\033[0;37m', # 8 - CINZA
)

def jump_line():
    print('\n')

def print_text_entralized(msg, cor=0):
    print(colors[cor], end='')
    print(f'{msg:^80}')
    print(colors[0], end='')

def print_line(cor=0, wid=0):
    print(colors[cor], end='')
    print('-=-'*wid)
    print(colors[0], end='')
