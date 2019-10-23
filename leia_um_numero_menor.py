"""
Faça um Programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.
    Observando os termos no plural a colocação do "e", da vírgula
    entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301,
    101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
print()
entrada = int(input('Entre com o número inteiro: '))

if(entrada <= 1000):

    print()
    centenas = (entrada // 100)
    dezenas = (entrada % 100) // 10
    unidades = ((entrada % 100) % 10) // 1

    print('{0} = {1} centenas, {2} dezenas e {3} unidades'.format(entrada, centenas, dezenas, unidades))

else:
    print('Entre com o número inteiro menor ou igual a 1.000')
