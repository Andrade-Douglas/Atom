"""
Faça um programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da area a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00self.
Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total.

"""

class Loja_Tintas:
    def __init__(self, area):
        self.area = area

    def numero_de_litros(self):
        global litros
        litros = self.area // 3
        if (self.area % 3 > 0):
            litros = litros + 1
        return litros

    def numero_de_latas(self):
        global latas
        latas = litros // 18
        if(litros % 18 > 0):
            latas = latas + 1
        return latas

    def imprime(self):
        print('QTD. UN.   VL_R$ TOTAL_R$')
        print(latas, '   latas', '80.0 ', latas * 80.0)

cliente1 = Loja_Tintas(54)
cliente2 = Loja_Tintas(55)
