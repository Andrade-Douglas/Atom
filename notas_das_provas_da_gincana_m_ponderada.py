'''
Questão 1 (PM MG). O Comandante da 500ª CIA PM promoveu um torneio operacional,
de forma que os militares da CIA PM foram divididos em 04 equipes para
realizarem 03 provas distintas, no valor de 10 pontos cada uma,
com os seguintes temas:
técnica policial-militar, abordagem a veículos e controle de distúrbios.
As provas teriam pesos 3, 2 e 1, respectivamente.

TABELA: notas das provas da gincana da 500ª CIA PM, por equipe e tema:
'''

import numpy as np

tecnica_policial_militar, abordagem_a_veiculos, controle_de_disturbios = np.loadtxt('C:/github/Atom/Project/Library_Numpy/notas_das_provas_da_gincana.csv',
                                                                                    delimiter=';',
                                                                                    unpack=True,
                                                                                    dtype='float')

media_ponderada = (((tecnica_policial_militar * 3) + (abordagem_a_veiculos * 2) + (controle_de_disturbios * 1))/(3 + 2 + 1))

print()
print('=' * 50)
print('Média Ponderada')
print('=' * 50)

for i in media_ponderada:
    print('Média ponderada: ', round(i,2))

print('=' * 50)
print('A menor média ponderada encontrada: ', np.amin(media_ponderada))
print('A maior média ponderada encontrada: ', np.amax(media_ponderada))
