minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

print("Minha lista: ", minha_lista)
print("Minha lista[5]: ", minha_lista[5])
print("Minha lista[1:7]: ", minha_lista[1:7])
print("Minha lista[:6]: ", minha_lista[:6])
print("Minha lista[2:]: ", minha_lista[2:])

#método append()
minha_lista.append(6)
print('Adicionando 6 ao final da lista: ', minha_lista)

#método index()
indice = minha_lista.index(6)
print('Índice do elemento 6: ', indice)

# método insert()
minha_lista.insert(2, 10)
print('Lista após a inserção: ', minha_lista)

# método pop()
elemento_removido = minha_lista.pop(3)
print('Elemento removido: ', elemento_removido)
print('Lista após pop(3): ', minha_lista)


# método remove
minha_lista.remove(6)
print('Minha lista após o remove(6): ', minha_lista)

# método sort
new_list = [1, 10, 35, 6, 2, 45]
new_list.sort()
print('Lista organizada de maneira crescente:', new_list)