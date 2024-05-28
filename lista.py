lista = [10, 5, 3, 4, 2, 7]
lista.sort() # coloca a lista em ordem crescente 
print(lista)

#lista[0] = 'a'
#print(lista)

print(f'Esse é o menor valor da lista', min(lista))
print(f'Esse é o maior valor da lista', max(lista))
print(f'Esse é a soma dos valores da lista', sum(lista))

lista.append(1)
print(f'Foi adicionado um novo valor ao fim da lsita', lista)

lista2 = [0, 1 ,2]
lista.extend(lista2)
print(lista)

del(lista[0])
print(f'O primeiro item foi excluído',lista)

lista.reverse()
print(f"Essa lista foi revertida", lista)



