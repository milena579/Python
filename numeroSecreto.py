print('JOGO DE ADIVINHAÇÃO')
numeroSecreto = 23
palpite = input('De o seu palpite: ')

if palpite.isdigit() == True:
    if palpite == numeroSecreto:
        print(f'Parabéns você acertou, o número era ', numeroSecreto)
    else:
         print('Você errou!')
else:
    print('Apenas números são aceitos')