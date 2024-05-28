import random
vitorias = 0
print("Escolha:")
op = {1:'PEDRA', 2:'PAPEL', 3:'TESOURA'}
resposta = int(input(f'Digite o que você deseja jogar:'))
pc = random.randint(1,3)


print(f'{pc}')
if resposta == pc:
    print(f'EMPATE! Foi escolhido {op[pc]} e {op[resposta]}')
else:
    if resposta == 1 and pc == 3:
        print(f'VOCE GANHOU! Voce jogou: {op[pc]} contra {op[resposta]}')
        vitorias = vitorias + 1
    else:
        print(f'VOCE PERDEU! Voce jogou: {op[pc]} contra {op[resposta]}')



