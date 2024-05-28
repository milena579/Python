import time
def contador(inicio, fim, passo):
    print(f'*' * 15, 'CONTADOR PASSO:', passo,  'INICIO:', inicio, 'FIM:', fim -1, '*' * 15 )

    for i in range(inicio, fim, passo):
            time.sleep(0.4)
            print(i)
contador(1,21,1)
contador(20,0,-2)
contador(0,106,5)
contador(96,53,-2)
contador(3,42,1)
contador(75,16,-5)
contador(390,40,-10)   
contador(inicio = int(input('Insira o início: ')), fim = int(input('Insira o fim: ', + 1)), passo = int(input('Insira o passo:')))
