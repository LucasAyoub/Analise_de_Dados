import numpy as np

# Considere os 3 arrays abaixo
# Retorne o valor do array xarr se o valor for True no array cond. Caso contrário, retorne o valor do array yarr.

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

for x, y, c in zip(xarr, yarr, cond):
    print(x, y, c)

resultado = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
resultado