import styleTextModule
import requests

styleTextModule.jumpLine()
styleTextModule.imprimirLinha(2,20)
styleTextModule.printTextCentralized('IMPORTAÇÃO E USO DE UM MÓDULO DE TERCEIROS',60,2)
styleTextModule.imprimirLinha(2,20)

url = 'https://www.google.com/'
response = requests.get(url)
styleTextModule.imprimirLinha(4,30)
styleTextModule.printTextCentralized(f'SOLICITAÇÃO HTTP PARA {url} RETORNOU STATUS {response.status_code}',90,4)
styleTextModule.imprimirLinha(4,30)
