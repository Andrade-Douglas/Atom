#Gerando base de dados .csv

from random import uniform
from random import randint

text = []

def getText():
    for i in range(1, 100):
        text.append(str(uniform(1.50, 2.20)) + ';' +
                    str(uniform(50, 120)) + ';' +
                    str(randint(0, 10)) + '\n')
def generateFile():
    file = 'C:/github/Atom/Project/Library_Numpy/weights.csv'
    enter = open(file, 'w+', encoding='UTF-8')
    getText()
    enter.writelines(text)
    enter.close()

if __name__ == '__main__':
    generateFile()
