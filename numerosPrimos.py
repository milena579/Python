while True:
    num = int(input('Digite um numero: '))
    list = []

    for i in range(1,num+1):
        if num % i == 0:
            list.append(i)
    list.append(num)
    if len(list) > 2:
        print(list)
        print('O número {} não é primo!!'. format(num))
    else: 
        print(list)
        print('O número {} é primo!'. format(num))

