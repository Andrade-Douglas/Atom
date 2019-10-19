"""
Faça um programa que peça um valor e mostre na tela se o valor é positivio ou
negativo.

"""

valor = int(input('Entre com um valor: '))

if(valor >= 0):
    print('{0} é positivo.'.format(valor))
else:
    print('{0} é negativo'.format(valor))
