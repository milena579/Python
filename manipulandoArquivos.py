import argparse
arquivo = 'texto.txt'

parser = argparse.ArgumentParser(description='programa exemplo')
parser.add_argument ('--arquivo',action='store', dest='arquivo', required=True, help='Arquivo')
parser.add_argument ('--palavraUsuario',action='store',dest='palavra', required=True, help='Palavra a ser procurada')

arguments = parser.parse_args()
arquivo = open(arguments.arquivo,'r')
palavraUsuario = (arguments.palavra)

c = 0
for linha in arquivo:
    linha = linha.strip()
    linha = linha.split(' ')

    for palavra in linha:
        if palavra == palavraUsuario:
            c = c + 1
print(f' A palavra, "{palavraUsuario}" aparece {c} vezes' )
