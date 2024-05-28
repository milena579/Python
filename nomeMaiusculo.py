#resposta = input("Insira seu nome: ")
#print(resposta[0:3].upper())

nomeUsuário = input("Insira seu nome completo em letras minusculas: ")
nomeMaiusculo = nomeUsuário.title()
nomeContagem = nomeUsuário.replace(" ", '')
print(nomeMaiusculo, f"\nSeu nome possui {len(nomeContagem)} de caracteres")
