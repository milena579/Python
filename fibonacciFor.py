num =  int(input('Digite o número de fatores: '))
valorAnterior = [0,1]
print(valorAnterior[0])
print(valorAnterior[1])
for i in range(0,num):
    valorAtual = valorAnterior[0] + valorAnterior[1]
    print(valorAtual)
    valorAnterior[0] = valorAnterior[1]
    valorAnterior[1] = valorAtual


#CORREÇÃO
    print('Série Fibonacci')
    print('-' * 30)

    while True:
        n =  int(input('Qual a quantidade de itens que deseja veriifcar? '))

        anterior = 0
        proximo = 1
        soma = 0
        list = []

        for i in range(0,n):
            list.append(anterior)
            soma = proximo + anterior 
            anterior =  proximo
            proximo = soma
        print(list)