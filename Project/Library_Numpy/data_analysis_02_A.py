# Analisando IMC

import numpy as np

def table(valIMC):
    if valIMC < 16:
        return str(valIMC) + ': Magreza grave'
    elif valIMC < 17:
        return str(valIMC) + ': Magreza moderada'
    elif valIMC < 18.5:
        return str(valIMC) + ': Magreza leve'
    elif valIMC < 25:
        return str(valIMC) + ': Saudável'
    elif valIMC < 30:
        return str(valIMC) + ': Sobrepeso'
    elif valIMC < 35:
        return str(valIMC) + ': Obesidade Grau I'
    elif valIMC < 40:
        return str(valIMC) + ': Obesidade Grau II (severa)'
    else:
        return str(valIMC) + ': Obesidade Grau III (mórbida)'

height, weigth, power = np.loadtxt('C:/github/Atom/Project/Library_Numpy/weights.csv',
                                   delimiter=';',
                                   unpack=True,
                                   dtype='float')
imc = weigth / height ** 2

print()
print('Mín: ', table(np.amin(imc)))
print('Máx: ', table(np.amax(imc)))
print('Máx - Mín: ', table(np.ptp(imc)))
print()
print('Média tradicinal: ', table(np.median(imc)))
print('Média por força: ', table(np.average(imc)))
print('Média aritmética: ', table(np.mean(imc)))
print('Desvio padrão: ', table(np.std(imc)))
print('Variânça: ', table(np.var(imc)))

print()
print(np.percentile(height, q=range(0,25)))

print('='*50)
print('Percentil')
print('='*50)
print('1º percentil ', table(np.median(np.percentile(imc, q=range(0,25)))))
print('2º percentil ', table(np.median(np.percentile(imc, q=range(26,50)))))
print('3º percentil ', table(np.median(np.percentile(imc, q=range(51,75)))))
print('4º percentil ', table(np.median(np.percentile(imc, q=range(76,100)))))

import matplotlib.pyplot as plt

y = []
x = [1,2,3,4]

y.append(np.median(np.percentile(imc, q=range(0,25))))
y.append(np.median(np.percentile(imc, q=range(26,50))))
y.append(np.median(np.percentile(imc, q=range(51,75))))
y.append(np.median(np.percentile(imc, q=range(76,100))))

plt.plot(x,y)
plt.title('Percentil dos IMC da População')
plt.ylabel('Valor')
plt.xlabel('Percentil')

plt.show()
