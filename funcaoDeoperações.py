import math
while True:
    def operacoes():
        numero = int(input('Digite um valor: '))
        raizQuadrada = math.sqrt(numero)
        quadrado = numero * numero
        inverso = 1 / numero
        fatorial = math.factorial(numero)

        return {'Raiz Quadrada':raizQuadrada ,'Quadrado': quadrado,'Inverso': inverso,'Fatorial':fatorial}
    
    resultados = operacoes()
    for i in resultados:
        print(f'{i} : {resultados[i]}\n')
    