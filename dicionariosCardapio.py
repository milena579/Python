print('Menu Fastfood')
cardapio = {'Hamburguer': 10, 'Hotdog': 6.5, 'Salada': 4, 'Suco': 4, 'Refrigerante': 4.5, 'Água': 2}
print(cardapio)
comida = cardapio[input(f'Digite a comida que você deseja: ' ).title()]
bebida = cardapio[input(f'Digite a bebida que você deseja: ').title() ]
print(f'O valor total é de:', comida + bebida)

