dados = open('dados.txt', encoding='utf8', mode='r')
dadosProcessados = open('dadosProcessados.txt', encoding='utf8', mode='w')
maiorMedia = 0
situacao = 'APROVADO'

for linha in dados:
    linha = linha.strip()
    linha = linha.split(",")
    print(linha)

    nomeAluno = linha[0] 
    notaUm = linha[1]
    notaDois = linha[2]
    notaTres = linha[3]

    notas = [float(notaUm), float(notaDois), float(notaTres)]
    media = (notas[0] + notas[1] + notas[2]) / 3 
    media = round(media, 2)

    if maiorMedia < media:
        maiorMedia = media

    if media < 7.0:
        situacao = 'REPROVADO'

    dadosProcessados.write(f'{nomeAluno}, {media}, {situacao} \n')

dadosProcessados.write(f'A maior MÉDIA foi do aluno(a):{nomeAluno}, com {media} de média \n')
dados.close
dadosProcessados.close


  








    
    

