class Process:
  def handle(self, username: str, password: str) -> None:
    if self.__verify_input_data(username, password): # 1
      self.__verify_input_in_database(username)
      self.__insert_new_user(username, password)
    else:
      self.__raise_error('Dados inválidos')

  # separando a validação em um local específico    
  def __verify_input_data(self, username: str, password: str) -> bool:
    return isinstance(username, str) and isinstance(password, str)
  
  def __verify_input_in_database(self, username: str) -> None:
    print('Acessando o banco de dados...') # 2
    print('Verificando existência do usuário...')

  def __insert_new_user(self, username: str, password: str) -> None:
    # adicionando novo user
    print(f'Cadastro de Usuário {username} => realizado com sucesso!')
    # print('Cadastro de usuários realizado com sucesso!') # 3

  def __raise_error(self, message: str) -> None:
    raise Exception(message)