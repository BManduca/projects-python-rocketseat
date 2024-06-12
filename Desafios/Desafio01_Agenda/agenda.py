from styleTextModule import jumpLine, imprimirLinha, printTextCentralized
import validNumerPhone
import time
from os import system

def add_contact(contacts_list, name_contact, phone_contact, email_contact):
    contact = {
        'contato': name_contact,
        'telefone': phone_contact,
        'email': email_contact,
        'favorito': False
    }
    contacts_list.append(contact)
    jumpLine()
    imprimirLinha(2,30)
    printTextCentralized(f'O contato {name_contact} foi adicionado com sucesso!',80,2)
    imprimirLinha(2,30)
    jumpLine()
    time.sleep(8)
    system('clear')
    return

def view_contacts(contacts_list):
    jumpLine()
    imprimirLinha(4,30)
    printTextCentralized('LISTA DE CONTATOS: ', 90,4)
    for index, contact in enumerate(contacts_list, start=1):
        name_contact = contact['contato']
        phone_contact = contact['telefone']
        email_contact = contact['email']
        favorite = '✓' if contact['favorito'] else ' '
        printTextCentralized(f'{index}. [{favorite}] [ {name_contact} | {phone_contact} | {email_contact} ]', 90, 4)
    imprimirLinha(4,30)
    jumpLine()
    time.sleep(4)
    system('clear')
    return

def showMenu():
    jumpLine()
    imprimirLinha(4,20)
    printTextCentralized('MENU DA AGENDA DE CONTATOS',60,4)
    jumpLine()
    printTextCentralized('1. SALVAR NOVO CONTATO', 60,4)
    printTextCentralized('2. VISUALIZAR CONTATOS', 60,4)
    printTextCentralized('3. EDITAR CONTATO', 60,4)
    printTextCentralized('4. MARCAR CONTATO COMO FAVORITO', 60,4)
    printTextCentralized('5. VISUALIZAR CONTATOS FAVORITOS', 60,4)
    printTextCentralized('6. DELETAR CONTATO', 60,4)
    printTextCentralized('7. FINALIZAR SISTEMA', 60,4)
    imprimirLinha(4,20)
    return

contacts = []

def main():
    while True:
        showMenu()
        jumpLine()

        actionChosen = '\nINSIRA A OPÇÃO DESEJADA: '
        choice = input(f'{actionChosen}')

        jumpLine()

        if choice == '1':
            name_contact = input('INSIRA O NOME DO NOVO CONTATO: ')
            print('\nO TELEFONE PRECISA SEGUIR O PADRÃO (99)99999-9999')
            phone_contact = input('TELEFONE: ')
            validNumerPhone.validationPhone(phone_contact)
            email_contact = input('INSIRA O EMAIL DO CONTATO: ')
            add_contact(contacts, name_contact, phone_contact, email_contact)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '7':
            jumpLine()
            imprimirLinha(3,20)
            printTextCentralized('FINALIZANDO SISTEMA...',60,3)
            imprimirLinha(3,20)
            jumpLine()
            time.sleep(3)
            system('clear')
            break

if __name__ == '__main__':
    main()