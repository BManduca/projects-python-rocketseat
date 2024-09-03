class Animal:
  def comer(self):
    print('O animal está comendo.')

  def  andar(self):
    print('O animal está andando na jaula.')

class Felino(Animal):
  def lamber(self):
    print('O felino está lambendo seu pelo.')

  # essa ação pode ser julgada como uma quebra do princípio de Liskov
  # def comer(self):
  #   print('O felino está comendo sua ração.')

class Leao(Felino):
  def rugir(self):
    print('O Leão está rugindo Alto!')

class Pessoa:
  def observa(self, animal: Animal):
    animal.comer()

animal = Animal()
felino = Felino()
renato = Pessoa()
leao = Leao()

renato.observa(leao)