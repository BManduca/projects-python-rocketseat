from styleTextModule import jumpLine, imprimirLinha, printTextCentralized
from validNumerPhone import validationPhone, printFormattedPhone
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
    time.sleep(6)
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
        printTextCentralized(f'{index}. [{favorite}] [ {name_contact} | {printFormattedPhone(phone_contact)} | {email_contact} ]', 90, 4)
    imprimirLinha(4,30)
    jumpLine()
    time.sleep(6)
    system('clear')
    return

def view_contacts_v2(contacts_list):
    jumpLine()
    imprimirLinha(4,30)
    printTextCentralized('LISTA DE CONTATOS: ', 90,4)
    for index, contact in enumerate(contacts_list, start=1):
        name_contact = contact['contato']
        phone_contact = contact['telefone']
        email_contact = contact['email']
        favorite = '✓' if contact['favorito'] else ' '
        printTextCentralized(f'{index}. [{favorite}] [ {name_contact} | {printFormattedPhone(phone_contact)} | {email_contact} ]', 90, 4)
    imprimirLinha(4,30)
    jumpLine()
    return

def edit_contact(contacts_list, index_contact, name_contact, phone_contact, email_contact):
    index_contact_edit = int(index_contact) - 1
    if len(contacts_list) > index_contact_edit >= 0:
        contacts_list[index_contact_edit]['contato'] = name_contact
        contacts_list[index_contact_edit]['telefone'] = phone_contact
        contacts_list[index_contact_edit]['email'] = email_contact
        jumpLine()
        imprimirLinha(5,20)
        printTextCentralized(f'O Contato {index_contact} - {contacts_list[index_contact_edit]['contato']} foi editado com sucesso.',60,5)
        imprimirLinha(5,20)
        jumpLine()
        time.sleep(5)
        system('clear')
    else:
        jumpLine()
        imprimirLinha(1,20)
        printTextCentralized('ÍNDICE DO CONTATO É INVÁLIDO',60,1)
        printTextCentralized('FAVOR INSERIR UM ÍNDICE DE CONTATO VÁLIDO!',60,1)
        imprimirLinha(1,20)
        jumpLine()
        time.sleep(5)
        system('clear')
    return

def check_favorite_contact(contacts_list, index_contact):
    index_contact_to_favorite = int(index_contact) - 1

    if len(contacts_list) > index_contact_to_favorite >= 0:
        contacts_list[index_contact_to_favorite]['favorito'] = True
        jumpLine()
        imprimirLinha(2,30)
        printTextCentralized(f'O CONTATO {index_contact} - {contacts_list[index_contact_to_favorite]['contato']} FOI MARCADO COMO FAVORITO.', 90, 2)
        imprimirLinha(2,30)
        jumpLine()
        time.sleep(5)
        system('clear')
    else:
        jumpLine()
        imprimirLinha(1,20)
        printTextCentralized('ÍNDICE DO CONTATO É INVÁLIDO',60,1)
        printTextCentralized('FAVOR INSERIR UM ÍNDICE DE CONTATO VÁLIDO!',60,1)
        imprimirLinha(1,20)
        jumpLine()
        time.sleep(5)
        system('clear')
    return

def view_contacts_favorites(contacts_list):
    jumpLine()
    imprimirLinha(2,30)
    printTextCentralized('LISTA DE CONTATOS FAVORITOS: ', 90,2)
    jumpLine()
    for index, contact in enumerate(contacts_list, start=1):
        if contact['favorito'] == True:
            name_contact = contact['contato']
            phone_contact = contact['telefone']
            email_contact = contact['email']
            printTextCentralized(f'{index}. [ {name_contact} | {printFormattedPhone(phone_contact)} | {email_contact} ]', 90, 2)
    imprimirLinha(2,30)
    jumpLine()
    time.sleep(5)
    system('clear')
    return

def delete_contact_by_index(contacts_list, index_contact):
    index_contact_to_delete = int(index_contact) - 1
    if len(contacts_list) > index_contact_to_delete >= 0:
        jumpLine()
        imprimirLinha(3,26)
        printTextCentralized(f'CONTATO {index_contact} - {contacts_list[index_contact_to_delete]['contato']} FOI DELETADO COM SUCESSO.',70,3)
        del contacts[index_contact_to_delete]
        imprimirLinha(3,26)
        jumpLine()
        time.sleep(5)
        system('clear')
    else:
        jumpLine()
        imprimirLinha(1,20)
        printTextCentralized('ÍNDICE DO CONTATO É INVÁLIDO',60,1)
        printTextCentralized('FAVOR INSERIR UM ÍNDICE DE CONTATO VÁLIDO!',60,1)
        imprimirLinha(1,20)
        jumpLine()
        time.sleep(5)
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
            validationPhone(phone_contact)
            email_contact = input('INSIRA O EMAIL DO CONTATO: ')
            add_contact(contacts, name_contact, phone_contact, email_contact)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            view_contacts_v2(contacts)
            contact_index = input('INSIRA O NÚMERO DO CONTATO QUE SERÁ EDITADO: ')
            contact_name = input('NOME: ')
            contact_phone = input('TELEFONE: ')
            contact_email = input('EMAIL: ')
            edit_contact(contacts, contact_index, contact_name, contact_phone, contact_email)
        elif choice == '4':
            view_contacts_v2(contacts)
            contact_index = input('INSIRA NÚMERO DO CONTATO QUE DESEJA MARCAR COMO FAVORITO: ')
            check_favorite_contact(contacts, contact_index)
        elif choice == '5':
            view_contacts_favorites(contacts)
        elif choice == '6':
            view_contacts_v2(contacts)
            contact_index = input('INSIRA NÚMERO DO CONTATO QUE DESEJA DELETAR: ')
            delete_contact_by_index(contacts, contact_index)
        elif choice == '7':
            jumpLine()
            imprimirLinha(3,20)
            printTextCentralized('FINALIZANDO SISTEMA...',60,3)
            imprimirLinha(3,20)
            jumpLine()
            time.sleep(1)
            system('clear')
            break
        else:
            jumpLine()
            imprimirLinha(1,20)
            printTextCentralized('OPÇÃO INVÁLIDA!',60,1)
            printTextCentralized('POR FAVOR INSIRA NOVAMENTE UMA OPÇÀO DO MENU!', 60, 1)
            imprimirLinha(1,20)
            time.sleep(5)
            system('clear')

if __name__ == '__main__':
    main()