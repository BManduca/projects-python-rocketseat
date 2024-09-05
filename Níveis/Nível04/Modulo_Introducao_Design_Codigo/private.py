class MyClass:

    # method public
    def registry(self) -> None:
        print('INICIANDO PROCESSO DE REGISTRO DE USUÁRIO..')
        self.__verify()
        self.__verify_register()
        self.__insert_data()

    # METHODS PRIVATE
    def __verify(self) -> None:
        print('VERIFICANDO DADOS DO USUÁRIO...')

    def __verify_register(self) -> None:
        print('VERIFICANDO REGISTRO DO USUÁRIO..')

    def __insert_data(self) -> None:
        print('INSERINDO DADOS DO USUÁRIO NO BANCO..')

obj = MyClass()

obj.registry()