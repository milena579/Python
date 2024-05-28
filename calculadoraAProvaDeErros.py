while True:
    try:

        primeiroNum = int(input('Digite o primeiro número: '))
        segundoNum = int(input('Digite o sugundo número: '))

        escolha = int(input('Digite:\n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n 0 - Sair\n '))


        if escolha == 1:
            print(f'O resultado é: ', primeiroNum + segundoNum)
        
        elif escolha == 2:
            print(f'O resultado é: ', primeiroNum - segundoNum)

        elif escolha == 3:
            print(f'O resultado é: ', primeiroNum  * segundoNum)

        try:
            if escolha == 4:
                print(f'O resultado é: ', primeiroNum / segundoNum)

        except ZeroDivisionError:
            print('O valor não pode ser dividido por 0')

    except ValueError:
        print('O valor inserido não é um número')

    digito = int(input('Digite 0 se quiser sair, ou para continuar digite qualquer valor: '))
    if escolha == 0 or digito == 0:
        break
