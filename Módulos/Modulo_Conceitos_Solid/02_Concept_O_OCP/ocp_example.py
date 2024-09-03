def printLine():
  print('-=-' * 20)

def printMessage(msg):
  print(f'{msg:^60}')

class Programmer:
  def make(self):
    printMessage('Programmer creating code...')

class Seller:
  def make(self):
    printMessage('Seller selling the product...')

class RH:
  def make(self):
    printMessage('Human Resources hiring new devs...')

class FrontEnd():
  def make(self):
    printMessage('Dev Front-End raising bugs in production...')

class Company:
  def do_work(self, worker: int) -> None:
    worker.make()
    # else:
    #   print('Error, no worker')

programmer = Programmer()
seller = Seller()
rh = RH()
frontend = FrontEnd()
company = Company()

printLine()
company.do_work(programmer)
company.do_work(seller)
company.do_work(rh)
company.do_work(frontend)
printLine()