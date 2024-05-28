
''' import random
    def listaOrdenada(li,ls,q):
        list = []
        for i in range(q):
            list.append(random.randint(li,ls))
        return list

    limiteInf = int(input('Digite o limite inferior: '))
    limiteSupe = int(input('Digite o limite inferior: '))
    tamanhoLista = int(input('Digite o tamanho da lista: ')) 

    lista = listaOrdenada(limiteInf,limiteSupe,tamanhoLista)
print(lista)  '''  

import random 
def listaOrdenada(li,ls,tl):
    list = []
    for i in range(tl):
        list.append(random.randint(li,ls))
        #print(list)
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                troca = list[j]
                list[j] = list[j+1] 
                list[j+1] = troca                
    return list    
    
limiteInfe = int(input('Digite o limite inferior:'))
limiteSup = int(input('Digite o limite superior:'))
tamanhoLista = int(input('Digite o tamanho da lista:'))

lista = listaOrdenada(limiteInfe, limiteSup, tamanhoLista)
print(lista)
