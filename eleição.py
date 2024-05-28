nasc = int(input('Qual ano você nasceu?: '))
anoAtual = 2024
idade = anoAtual - nasc
if idade < 16:
    print('Você ainda não pode votar')
elif idade < 18 or idade >= 70:
    print('Seu voto é facultativo')
else:
    print('Você TEM que votar!')