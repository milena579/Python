import re, random

textoPalavras = open('palavrasSecretas.txt', encoding='utf8', mode='r')
p = textoPalavras.read()
palavrasSecretas = re.split(r'[\s\n,?:!-]+', p.lower())

palavrasFaceis = []
palavrasMedias = []
palavrasDificil = []


for palavra in palavrasSecretas:
    if len(palavra) <= 5:
        palavrasFaceis.append(palavra)

    elif len(palavra) == 7:
        palavrasMedias.append(palavra)   

    else:
        palavrasDificil.append(palavra)    

def jogar():
    pontos = 100

    listaEmbaralhada = []
    while True:
        try:
            print(f'-'*15, 'PALAVRAS EMBARALHADAS', '-'*15)
            print('FÁCIL : 1, MÉDIO: 2, DIFÍCIL: 3 ')

            nivel = int(input('Digite o nível que vc deseja: '))

            if nivel == 1:
                palavraSecreta = palavrasFaceis[random.randint(0,len(palavrasFaceis))]

            elif nivel == 2:
                palavraSecreta = palavrasMedias[random.randint(0,len(palavrasMedias))]

            elif nivel == 3:
                palavraSecreta = palavrasDificil[random.randint(0,len(palavrasDificil))]

            listaEmbaralhada.append(palavraSecreta)
            listaEmbaralhada = list(palavraSecreta)
            random.shuffle(listaEmbaralhada)
            palavraEmbaralhada = ' '.join(listaEmbaralhada)
            #print(palavraSecreta)
            try:    
                for tentativa in range (1,6):     
                    print(f'{palavraEmbaralhada} \n')
                    palpite = str(input('De o seu palpite: '))

                    if palpite == palavraSecreta:
                        print(f'Parabéns, você acertou!')
                        print(f'A palavra era {palavraSecreta}')
                        print(f'Você acertou na sua {tentativa}° tentativa')
                        print(f'Sua pontuação ficou em {pontos} de 100 pontos \n')

                    elif palpite != palavraSecreta:
                        pontos = pontos - 20
                        print(f'Sua pontuação ficou em {pontos} de 100')
                        print(f'Essa foi sua {tentativa}° tentativa \n')

                    elif pontos == 0:
                        print(f'VOCÊ PERDEU! \n A palavra secreta era "{palavraSecreta}"')
                        print(f'Pontos = {pontos}')

                    tentativa = tentativa + 1

                    if palpite == palavra:
                        break 
            except ValueError:
                print('Apenas letras')

        except ValueError:
            print('Opção inválida')
            
jogar()
        



 

   
   
   