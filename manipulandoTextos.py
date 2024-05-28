import re
texto = open('texto.txt', encoding='utf8', mode='r')
p = texto.read()
palavras = re.split(r'[\s\n,?:!-]+', p.lower())
lista = []
contagem = 0
for palavra in palavras:
    if palavra not in lista:
        lista.append(palavra)
        contagem = contagem + 1

print(lista)
print(contagem)

