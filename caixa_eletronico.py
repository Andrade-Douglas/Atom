"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
usuário o valor do saque e depois informar quantas notas de cada valor
serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na
máquina.
    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
    notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
    três notas de 100, uma nota de 50, quatro notas de 10,
    uma nota de 5 e quatro notas de 1.
"""

print()

saque = int(input('Entre com o valor a ser sacado: '))

if(saque >= 10) and (saque <= 600):

    print()
    print('Processando...')
    print('Valor autorizado!')

    quantidade_nota_cem = saque // 100
    quantidade_nota_cinquenta = (saque % 100) // 50
    quantidade_nota_dez = ((saque % 100) % 50) // 10
    quantidade_nota_cinco = (((saque % 100) % 50) % 10) // 5
    quantidade_nota_um = ((((saque % 100) % 50) % 10) % 5) // 1

    print()
    print('As cedulas de R$ 100.00 estão disponives na quantidade: {0}'.format(quantidade_nota_cem))
    print('As cedulas de R$  50.00 estão disponives na quantidade: {0}'.format(quantidade_nota_cinquenta))
    print('As cedulas de R$  10.00 estão disponives na quantidade: {0}'.format(quantidade_nota_dez))
    print('As cedulas de R$   5.00 estão disponives na quantidade: {0}'.format(quantidade_nota_cinco))
    print('As cedulas de R$   1.00 estão disponives na quantidade: {0}'.format(quantidade_nota_um))

else:

    print('O valor mínimo de saque é de R$ 10.00 e o máximo de R$ 600.00')
