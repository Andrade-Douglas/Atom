"""
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 4 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 4 litros;
    misturar latas e galões, de forma que o preço seja o menor.

Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias

"""
print()
area = int(input('Entre com o tamanho em metros quadrados da área a ser pintada: '))
area = area * 1.1
print()
sobra = ((area / 6) - (area // 6))

#Vamos calcular o numero de litros necessários para pintar a casa
litros = area // 6
if(area % 6 > 0):
    litros += 1

#Vamos calcular o numero de latas necessários para pintar a casa
latas = litros // 18
if(litros % 18 > 0):
    latas += 1
    
print('A area a ser pintada com 10% de folga: {0}'.format(int(area) + 1))
print('Litros necessários: {0}'.format(litros))
print()
print('Latas necessárias: {0}'.format(latas))
print('Total: R$', latas * 80.0)

# GALÕES
#Vamos calcular o numero de litros necessários para pintar a casa
galoes = litros // 4
if(litros % 4 > 0):
    galoes += 1

print()
print('Galões necessárias: {0}'.format(galoes))
print('Total: R$', galoes * 25.0)

#Vamos calcular a melhor compra entre os dois
print()
print('Vender latas e galões de forma que o custo seja o menor')
latas = litros // 18
galoes = 0
litros_sobras = litros % 18

if (litros_sobras) <= 3 * 4:
    #Ou seja o numero de galoes necessarios seja menor do que três
    galoes = litros_sobras // 4
    if (litros_sobras % 4 > 0):
        galoes += 1
else:
    latas += 1

print('Latas necessárias: {0}'.format(latas))
print('Galões necessárias: {0}'.format(galoes))
print('Total: R$ {0}'.format(galoes * 25 + latas * 80))
