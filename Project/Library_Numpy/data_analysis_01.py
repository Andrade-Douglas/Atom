import numpy as np

heights = [1.72, 1.56, 1.45, 1.56, 1.65, 1.70]
weights = [86.5, 48.0, 56.0, 70.5, 80.2, 65.7]

nHeights = np.array(heights)
nWeights = np.array(weights)

imcs = nWeights / nHeights ** 2

print()
for imc in imcs:
    imc_ = round(imc, 2)

    print('IMC: {0}'.format(imc_))
