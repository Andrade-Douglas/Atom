'''
Questão 1 (PM MG). O Comandante da 500ª CIA PM promoveu um torneio operacional,
de forma que os militares da CIA PM foram divididos em 04 equipes para
realizarem 03 provas distintas, no valor de 10 pontos cada uma,
com os seguintes temas:
técnica policial-militar, abordagem a veículos e controle de distúrbios.
As provas teriam pesos 3, 2 e 1, respectivamente.

TABELA: notas das provas da gincana da 500ª CIA PM, por equipe e tema:
'''

from random import uniform
from random import randint

results = []

def getResults():
    for i in range(1,100):
        results.append(str(uniform(0,10)) + ';' +
                    str(uniform(0,10)) + ';' +
                    str(uniform(0,10)) + '\n')

def generateFile():
    file = 'C:/github/Atom/Project/Library_Numpy/notas_das_provas_da_gincana.csv'
    enter = open(file, 'w+', encoding='UTF-8')
    getResults()
    enter.writelines(results)
    enter.close()

if __name__ == '__main__':
    generateFile()
