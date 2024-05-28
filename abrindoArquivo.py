
palavraUsuario = str(input('Digite uma palavra para procurar na lista: '))
arquivo = open('arquivo.txt', encoding='utf-8', node='r')

c = 0
for linha in arquivo:
    linha = linha.strip()
    print(linha)
    linha = linha.split(' ')
    print(linha)

    for palavra in linha:
        if palavra == palavraUsuario:
            c = c + 1
print(f' A palavra "',palavraUsuario,'"aparece', c, 'vezes' )
    