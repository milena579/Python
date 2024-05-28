import random
vitorias = 0

while True: 
    pc = random.randint(1,10)
    jogador = int(input('Digite um número: '))
    opcao = input('\nPAR ou IMPAR?: ').lower()
    soma = jogador + pc
    sair = 1
 
    if opcao == 'impar' and soma % 2 != 0 or opcao == 'par'and soma % 2 == 0:
        print(f'A soma foi', soma)
        print('Você venceu! \n' )
    else: 
        print(f'A soma foi', soma)
        print('Você perdeu!')
        print(f'O número de vitórias foi:',vitorias)
        sair = int(input('\nDigite 0 para sair: '))

    vitorias =  vitorias + 1
    if sair == 0 : break
    

    

    

    
    