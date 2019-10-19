"""
Faça um programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da area a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00self.
Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total.

"""
area = int(input('Entre com o tamanho em metros quadrados da area a ser pintada: '))
print()

litros = area // 3
if area % 3 > 0:
    litros = litros + 1

latas = litros // 18
if litros % 18 > 0:
    latas = latas + 1

preco_lata = 80.00

print('QTD. UN.   VL_R$ TOTAL_R$')
print(latas, '   latas', '80.0 ', latas * preco_lata)
