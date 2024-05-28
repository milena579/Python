contador = 1;
soma = 0
#while a <= 5:
    #print(a)
    #a += 1

limite = int(input('Digite qual é o limite: '))

while contador <= limite:
    soma = soma + contador
    contador = contador + 1

print(f'O valor total da soma é: ', soma) 