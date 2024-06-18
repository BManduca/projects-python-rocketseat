from styleGameModule import jumpLine, printTextCentralized, imprimirLinha
import time
import random
from os import system

# Personagem: classe mãe

# Herói: vai herdar tudo do da classe mãe Personagem e vai ser controlado pelo usuário

# Inimigo: vai herdar tudo da classe mãe Personagem e vai ser controlado pelo adversário

# Pilares utilizados: Encapsulamento, Herança e polimorfismo

class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        # atríbutos
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    # principais métodos
    def get_name(self):
        return self.__nome
    
    def get_life(self):
        return self.__vida
    
    def get_level(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f'Nome: {self.get_name()} | Vida: {self.get_life()} | Nivel: {self.get_level()}'
        # printTextCentralized(f'Nome: {self.get_nome()}', 40, 5)
        # printTextCentralized(f'Vida: {self.get_vida()}', 40, 5)
        # printTextCentralized(f'Nível: {self.get_nivel()}', 40, 5)
        

    def receive_attack(self, damage):
        self.__vida -= damage

        if self.__vida < 0:
            self.__vida = 0

    def attack(self, target):
        # baseado no nível do personagem
        damage = random.randint(self.get_level() * 2, self.get_level() * 4)
        target.receive_attack(damage)
        jumpLine()
        imprimirLinha(6,30)
        printTextCentralized(f'{self.get_name()} atacou {target.get_name()} e causou {damage} de dano!', 90, 6)
        imprimirLinha(6,30)


    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__skill = habilidade

    def get_skill(self):
        return self.__skill
    
    def exibir_detalhes(self):
        jumpLine()
        imprimirLinha(3,30)
        printTextCentralized(f'{super().exibir_detalhes()} | Habilidade: {self.get_skill()}', 90, 3)
        imprimirLinha(3,30)

    def special_attack(self, target):
        # dano aumentado
        damage = random.randint(self.get_level() * 5, self.get_level() * 8)
        target.receive_attack(damage)
        jumpLine()
        imprimirLinha(7,30)
        printTextCentralized(f'{self.get_name()} usou a habilidade especial {self.get_skill()} em {target.get_name()} e causou {damage} de dano!', 90, 7)
        imprimirLinha(7,30)


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_type(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        imprimirLinha(2,30)
        printTextCentralized(f'{super().exibir_detalhes()} | Tipo: {self.get_type()}', 90, 2)
        imprimirLinha(2,30)

class Game:
    round = 0

    ''' CLASSE ORQUESTRADORA DO JOGO '''
    def __init__(self) -> None:
        self.heroi = Heroi(nome='Homem-aranha', vida=100, nivel=6, habilidade='Soco venom')
        self.inimigo = Inimigo(nome='Kraven', vida=120, nivel=6, tipo='Caçador')

    def play_battle(self):
        ''' REALIZAR A GESTÃO DA BATALHA EM TURNOS '''
        imprimirLinha(4,30)
        printTextCentralized('INICIANDO A BATALHA!',90,4)
        imprimirLinha(4,30)
        jumpLine()

        while self.heroi.get_life() > 0 and self.inimigo.get_life() > 0:
            self.round += 1
            imprimirLinha(4,30)
            printTextCentralized(f'RODADA {self.round}',90,4)
            imprimirLinha(4,30)
            imprimirLinha(5,30)
            printTextCentralized('DETALHES DOS PERSONAGENS: ',90,5)
            imprimirLinha(5,30)
            self.heroi.exibir_detalhes()
            self.inimigo.exibir_detalhes()

            jumpLine()
            input('PRESSIONE ENTER PARA ATACAR...')
            # printTextCentralized('ESCOLHA (1 - ATAQUE NORMAL, 2 - ATAQUE ESPECIAL): ', 90, 4)
            choice = input('ESCOLHA (1 - ATAQUE NORMAL, 2 - ATAQUE ESPECIAL): ')

            if choice == '1':
                self.heroi.attack(self.inimigo)
            elif choice == '2':
                self.heroi.special_attack(self.inimigo)
            else:
                printTextCentralized('ESCOLHA INVÁLIDA. POR FAVOR ESCOLHA NOVAMENTE!', 90, 2)

            # inimigo atacando o heroi
            if self.inimigo.get_life() > 0:
                # inimigo ataca o herói
                self.inimigo.attack(self.heroi)

            time.sleep(4)
            system('clear')
        
        if self.heroi.get_life() > 0:
            jumpLine()
            imprimirLinha(3,30)
            printTextCentralized('PARABÉNS, VOCÊ VENCEU A BATALHA!', 90, 3)
            imprimirLinha(3,30)
        else:
            imprimirLinha(2,30)
            printTextCentralized('VOCÊ FOI DERROTADO!', 90, 2)
            imprimirLinha(2,30)


# heroi = Heroi(nome='Homem-aranha', vida=150, nivel=6, habilidade='Soco venom')
# heroi.exibir_detalhes()

# inimigo = Inimigo(nome='Kraven', vida=120, nivel=3, tipo='Caçador')
# inimigo.exibir_detalhes()

# CRIANDO INSTÂNCIA DO JOGO E INICIAR BATALHA
game = Game()
game.play_battle()
